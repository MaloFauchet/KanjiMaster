import ctypes
import os
import sys
from random import choice


class Main:
    def __init__(self):
        self.path = os.path.abspath(os.path.dirname(sys.argv[0]))
        self.backchoice = ""
        for root, directories, files in os.walk(os.path.join(self.path, 'backgrounds')):
            self.backgrounds = [file.lower() for file in files if file.endswith(('.png', '.jpg', '.jpeg'))]
        self.backchoice = choice(self.backgrounds)
        ctypes.windll.user32.SystemParametersInfoW(0x14, 0,  f"D:/Divers/Python/Desktop Background Changer/backgrounds/{self.backchoice}", 0x2)
        

application = Main()
