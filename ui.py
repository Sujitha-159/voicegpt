from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from main import adele

class ContentGenerationApp(App):
    def build(self):
        layout = FloatLayout()

        # Add a background image to cover the entire application window
        background = Image(source='images/bg.gif', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)

        self.start_button = Button(
            text="Start",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.6}
        )
        self.start_button.bind(on_press=self.start_content_generation)
        layout.add_widget(self.start_button)

        self.stop_button = Button(
            text="Stop",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.4}
        )
        self.stop_button.bind(on_press=self.stop_content_generation)
        layout.add_widget(self.stop_button)

        self.content_generating = False

        return layout

    def start_content_generation(self, instance):
        self.content_generating = True
        self.start_button.disabled = False
        self.stop_button.disabled = False
        adele()

    def stop_content_generation(self, instance):
        self.content_generating = False
        self.start_button.disabled = False
        self.stop_button.disabled = False
        adele().quit()

if __name__ == '__main__':
    ContentGenerationApp().run()
