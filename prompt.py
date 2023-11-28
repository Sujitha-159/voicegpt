import openai
import pyttsx3

openai.api_key='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'

engine=pyttsx3.init()
def generate_response(prompt):
    response=openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=5000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response["choices"][0]["text"]

x=generate_response("hiii")
print(x)