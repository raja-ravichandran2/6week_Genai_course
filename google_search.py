import pyautogui
import time
import subprocess

# -----------------------------------
# STEP 1: Open Chrome Browser
# -----------------------------------

print("Opening Chrome...")

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

subprocess.Popen(chrome_path)

# Wait for Chrome to open
time.sleep(2)

# -----------------------------------
# STEP 2: Open Google
# -----------------------------------

print("Opening Google...")

# Focus address bar
pyautogui.hotkey('ctrl', 'l')

time.sleep(1)

# Type Google URL
pyautogui.write("https://www.google.com", interval=0.05)

# Press Enter
pyautogui.press("enter")

time.sleep(2)

# -----------------------------------
# STEP 3: Search Text
# -----------------------------------

print("Searching for IPL stats...")

# Type search query
pyautogui.write("yesterday ipl match stats", interval=0.05)

time.sleep(1)

# Press Enter
pyautogui.press("enter")

# Wait for search results
time.sleep(2)

# -----------------------------------
# STEP 4: Click First Search Result
# -----------------------------------

print("Clicking first result...")

# Press TAB multiple times
# until first result is selected
location = pyautogui.click(534, 534)  # Click on the search results area to ensure it's focused
pyautogui.click(location)
pyautogui.scroll(-7900)  # Scroll down to ensure the first result is visible
pyautogui.sleep(2)
imagelocation = pyautogui.locateCenterOnScreen('iplplay.png', confidence=0.5, grayscale=True)  # Locate the first result on the screen
print(imagelocation)
pyautogui.click(imagelocation)  # Click on the first result
print("Done.")