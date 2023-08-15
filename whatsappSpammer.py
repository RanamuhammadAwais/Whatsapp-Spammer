import pyautogui

pyautogui.sleep(3)
for i in range(1,30):
    pyautogui.sleep(0.1)
    pyautogui.write("Good night !!  ")
    pyautogui.hotkey("enter")
