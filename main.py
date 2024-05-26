from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from datetime import datetime

import PIL

kv = '''
<ScreensManager>:
    MainScreen:
    CameraScreen:

<MainScreen>:
    name: "main"
    FloatLayout:
        Button:
            text: "Open Camera"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            size_hint: 0.9, 0.2
            on_release: root.manager.current = "camera"

<CameraScreen>:
    name: "camera"
    FloatLayout:
        Camera:
            id: camera
            resolution: (640, 480)
            play: True
        Button:
            text: "Take a Picture"
            size_hint: 0.2, 0.1
            pos_hint: {"center_x": 0.5, "y": 0.1}
            on_release: root.capture_image()
        Button:
            text: "Back to Main Screen"
            size_hint: 0.2, 0.1
            pos_hint: {"center_x": 0.5, "y": 0.2}
            on_release: root.manager.current = "main"
'''

class ScreensManager(ScreenManager):
    pass

class MainScreen(Screen):
    pass

class CameraScreen(Screen):
    def capture_image(self):
        camera = self.ids.camera
        current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = f"screenshot_{current_time}.png"

        camera.export_to_png(filename)

        # Additional image processing with PIL
        img = PIL.Image.open(filename)
        img.show()  # Example: Display the captured image

class CameraApp(App):
    def build(self):
        sm = ScreensManager()
        sm.add_widget(MainScreen())
        sm.add_widget(CameraScreen())
        return sm

if __name__ == '__main__':
    CameraApp().run()