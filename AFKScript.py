import pyautogui
import keyboard
import time

print("start")

#start = pyautogui.locateOnScreen("reload.png")
#print(start)
#pyautogui.moveTo(start)

"""while 1:
    if pyautogui.locateOnScreen("Server.png",confidence = 0.7):
        print("ye")
        time.sleep(0.5)
    else:
        print("nah")
        time.sleep(0.5)"""
try :

    while 1:
        if pyautogui.locateOnScreen("Reload.png",confidence = 0.85) :
            pyautogui.moveTo(pyautogui.locateOnScreen("Reload.png",confidence = 0.85))
            pyautogui.click()

        elif pyautogui.locateOnScreen("Server.png",confidence = 0.85):
            pyautogui.moveTo(pyautogui.locateOnScreen("Server.png",confidence = 0.85))
            pyautogui.click()
            time.sleep(0.25)
            pyautogui.moveTo(pyautogui.locateOnScreen("join.png",confidence = 0.85))
            pyautogui.click()
            
        
        else:
            print("welp")
            time.sleep(0.5)
except KeyboardInterrupt:
    print("Code Ended")
