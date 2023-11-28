import tkinter as tk
import threading
import speech_recognition as sr
import pyttsx3
import openai

# Set your OpenAI API key
openai.api_key = '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'

# Initialize the Tkinter app
root = tk.Tk()
root.title("Speech-to-Text & Prompt Generation")

# Initialize the speech recognition engine
recog = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Variables to control recording and prompt generation
recording = False
generation = False

# Function to handle audio recording and prompt generation
def record_and_generate():
    global recording, generation
    while recording:
        with sr.Microphone() as source:
            print("Speak Anything:")
            recog.adjust_for_ambient_noise(source)
            try:
                audio = recog.listen(source)
                print("Audio recording completed")
                txt = recog.recognize_google(audio)
                print(f"Transcription: {txt}")
                if generation:
                    response = generate_response(txt)
                    speak_text(response)
            except Exception as e:
                print("An unknown exception has occurred")

# Function to start or stop audio recording and prompt generation
def toggle_recording_generation():
    global recording, generation
    if not recording:
        recording = True
        generation = True
        threading.Thread(target=record_and_generate).start()
        start_button.config(state=tk.DISABLED)
        stop_button.config(state=tk.NORMAL)
    else:
        recording = False
        generation = False
        start_button.config(state=tk.NORMAL)
        stop_button.config(state=tk.DISABLED)

# Function to generate a response using OpenAI
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=25,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response["choices"][0]["text"]

# Function to speak text using the text-to-speech engine
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Create buttons
start_button = tk.Button(root, text="Start Recording", command=toggle_recording_generation)
stop_button = tk.Button(root, text="Stop Recording", command=toggle_recording_generation)
stop_button.config(state=tk.DISABLED)

# Layout
start_button.pack()
stop_button.pack()

# Run the Tkinter main loop
root.mainloop()
