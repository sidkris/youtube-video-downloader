from kivymd.app import MDApp
from kivy.lang import Builder
from app_logic import YouTubeDownloader
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


KV = '''
MDScreen:

    MDTextField:
        id: text_input
        hint_text: "Enter URL here"
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        size_hint_x: 0.6

    MDRectangleFlatButton:
        id: submit_button
        text: "DOWNLOAD"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

'''

class MyApp(MDApp):

    title = "YouTube Downloader"

    def build(self):
        self.my_utils = YouTubeDownloader()
        screen = Builder.load_string(KV)

        screen.ids.submit_button.bind(on_press=self.handle_button_click)
        # screen.ids.call_method_button.bind(on_press=self.my_utils.download_video)

        return screen

    def handle_button_click(self, instance):
        text = self.root.ids.text_input.text  # Get the input text
        self.my_utils.download_video(text)  # Pass the text to the external method
        self.show_popup()
    
    def show_popup(self):
        dialog = MDDialog(
            title = "Success!",
            text = "VIDEO SUCCESSFULLY DOWNLOADED"
        )
        dialog.open()

if __name__ == '__main__':
    MyApp().run()
