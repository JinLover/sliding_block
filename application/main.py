from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.texture import Texture

# Pyjnius를 사용하여 Android의 네이티브 API 호출
from jnius import autoclass

class ScreenControlApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        # 스크린샷 버튼
        self.screenshot_button = Button(text="Capture Screen")
        self.screenshot_button.bind(on_press=self.capture_screen)
        self.layout.add_widget(self.screenshot_button)
        
        # 스크린샷 결과 표시
        self.image = Image()
        self.layout.add_widget(self.image)
        
        return self.layout

    def capture_screen(self, instance):
        # Android의 SurfaceControl API를 사용하여 화면 캡처
        try:
            # SurfaceControl API 접근 (Android 10 이상 필요)
            SurfaceControl = autoclass('android.view.SurfaceControl')
            Bitmap = autoclass('android.graphics.Bitmap')
            activity = autoclass('org.kivy.android.PythonActivity').mActivity

            # 현재 화면 캡처
            screenshot = SurfaceControl.screenshot(1080, 1920)  # 해상도 설정
            bitmap = Bitmap.createBitmap(screenshot)

            # Bitmap -> Kivy 텍스처 변환
            width, height = bitmap.getWidth(), bitmap.getHeight()
            pixels = bitmap.getPixels()
            texture = Texture.create(size=(width, height))
            texture.blit_buffer(pixels, colorfmt='rgba', bufferfmt='ubyte')

            # 캡처 결과를 Image 위젯에 표시
            self.image.texture = texture
        except Exception as e:
            print(f"Error capturing screen: {e}")

if __name__ == "__main__":
    ScreenControlApp().run()