from kivy.app import App
from kivy.uix.button import Button
import plyer

class myapp(App):
    def build(self):
        return Button(text='Notification', on_press=self.notify)
    
    def notify(self, obj):
        plyer.notification.notify(title="My App", message="Test Notification")

myapp().run()
