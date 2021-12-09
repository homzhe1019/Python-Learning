from pymouse import PyMouse
from pykeyboard import PyKeyboard
import pyperclip
import time
import os

m = PyMouse()
k = PyKeyboard()
os.startfile('C:\\Users\\LIM\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')
time.sleep(3)
m.click(580, 350)
time.sleep(3)
k.type_string('6196192519')
time.sleep(0.5)
m.click(580, 350)
m.click(580, 350)
m.click(580, 350)
k.tap_key(k.backspace_key)
pyperclip.copy('林泓喆')
k.press_key(k.control_key)
k.tap_key('v')
k.release_key(k.control_key)
m.click(500, 450)
m.click(630, 525)
time.sleep(3)
k.type_string('619619')
time.sleep(1)
k.tap_key(k.enter_key)



