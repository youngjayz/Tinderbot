import pyautogui
import webbrowser
import time

"""
Free Version: 100 swipes per 12-hour period.
Paid Version: Unlimited swipes
How to: User must be logged in prior start
        Works best when in full screen mode in browser"""

url = r'https://tinder.com'

# MacOS
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows1
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# Linux
# chrome_path = '/usr/bin/google-chrome %s'

webbrowser.get(chrome_path).open(url)
time.sleep(2)
pyautogui.click(button='left')
time.sleep(2)

for x in range(0, 200):
    pyautogui.press('right')
    if x == 100:
        print("Exit Program")
        break
    print(x)
