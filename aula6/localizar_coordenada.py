import pyautogui

xy = pyautogui.locateOnScreen ("aula6\\bnt_8.png",
                               confidence=0.5)

print (xy)

