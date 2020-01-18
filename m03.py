from microbit import *
import music

tune = ["C4:4", "C4:4", "G4:4", "G4:4", "A4:4", "A4:4", "G4:8", "F4:4",
        "F4:4", "E4:4", "E4:4", "D4:4", "D4:4", "C4:8", "G4:4", "G4:4", "F4:4", "F4:4", "E4:4", "E4:4", "D4:8", "G4:4",
        "G4:4", "F4:4", "F4:4", "E4:4", "E4:4", "D4:8", "C4:4", "C4:4", "G4:4", "G4:4", "A4:4", "A4:4", "G4:8", "F4:4",
        "F4:4", "E4:4", "E4:4", "D4:4", "D4:4", "C4:8"]
        
while True:
    if button_a.is_pressed():
        music.play(tune)