from PIL import ImageGrab
from StringIO import StringIO
import pyautogui

class RemoteDesktop:
    def __init__(self):
        self.size = pyautogui.size()
        self.quality = 50

    def changeQuality(self, quality):
        self.quality = quality
        return quality
        
    def getPicture(self):
        screen = ImageGrab.grab()
        buf = StringIO()
        screen.save(buf, 'JPEG', quality=self.quality)
        buf.seek(0)
        return buf

    def getSize(self):
        return self.size

    def click(self, x, y, button="left"):
        pyautogui.click(x=x, y=y, button=button)

    def typewrite(self, data):
        pyautogui.typewrite(data)