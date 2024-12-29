# The AI Virtual Keyboard
#  DONE BY:-  SUBHAM KEWAT

import cv2
from HandTracking import HandDetector
from time import sleep
import numpy as np
import cvzone
from pynput.keyboard import Controller

# Open the camera (0 is usually the default camera)
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720) 

detector = HandDetector(detectionCon=0.8) 

keys = [["1", "2", "3", "4", "5", "6", "7", "8", "9", "0","Backspace"],
        ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P","[","]"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";","'"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"],]
        
finalText = ""
 
keyboard = Controller()
  

def drawKeyboard(img, buttonList):
    imgNew = np.zeros_like(img, np.uint8)
    for button in buttonList:
        x, y = button.pos
        cvzone.cornerRect(imgNew, (button.pos[0], button.pos[1], button.size[0], 
                                button.size[1]),20, rt=0)
        cv2.rectangle(imgNew, button.pos, (x + button.size[0],y + button.size[1]),
                                (0, 51, 51), cv2.FILLED)  
        cv2.putText(imgNew, button.text, (x + 40, y + 60),
                                cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3)

    out = img.copy()
    alpha = 0.5
    mask = imgNew.astype(bool)
    out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]
    return out
 
 
class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text


buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        # Special case for "Backspace" key to make them larger
        
        if key == "Backspace":
            buttonList.append(Button([100 * 2 + 850, 100 * i + 50], key, size=[210, 95]))
        else:
            buttonList.append(Button([100 * j + 50, 100 * i + 50], key))
 
while True:
    success, img = cap.read()
    flipped_frame = cv2.flip(img, 1)          #flip for the camera.............
    img = detector.findHands(flipped_frame) 
    lmList = detector.findPosition(img)
    img = drawKeyboard(img, buttonList)

    if lmList:
        for button in buttonList:
            x, y = button.pos
            w, h = button.size

            if x < lmList[8][1] < x + w and y < lmList[8][2] < y + h:
                cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (175, 0, 175), cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 65),
                            cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                long, _, _ = detector.findDistance(8, 12, img, draw=True)
                
                if long < 30:
                    # Press regular keys
                    if button.text not in ["Backspace"]:
                        keyboard.press(button.text)
                        cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                        cv2.putText(img, button.text, (x + 20, y + 65),
                                cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                        finalText += button.text        
                    # Handle Backspace key
                    elif button.text == "Backspace":
                        # keyboard.press(button.text)
                        finalText = finalText[:-1] if finalText else finalText
                    sleep(0.8)  
 
    cv2.rectangle(img, (50, 540), (1240, 450), (51, 0, 102), cv2.FILLED)
    cv2.putText(img, finalText, (50, 520),
                cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)
 
    cv2.imshow("Image", img)
    cv2.waitKey(1)
