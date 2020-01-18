# Add your Python code here. E.g.
from microbit import *


while True:
    if button_a.is_pressed():
        display.show('A')
    
    if button_b.is_pressed():   
        display.show('B')
    
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(Image.HEART)
        sleep(2000)
