import time # lets the script pause for short moments.
import pyautogui # controls the mouse and keyboard, and takes screenshots.
from PIL import ImageOps # rom Pillow, used here to convert images to grayscale.

# Adjust these if needed for your screen size / browser scale
THRESHOLD = 120 # pixel brightness threshold to detect obstacles
SCAN_WIDTH = 140 # width of the area to scan for obstacles (adjust based on game speed)
SCAN_HEIGHT = 30 # height of the area to scan for obstacles (adjust based on game speed)
OFFSET_X = 80 # horizontal offset from the dino to start scanning (adjust based on game speed)
OFFSET_Y = 10 # vertical offset from the dino to start scanning (adjust based on game speed)

def calibrate(): # this function “calibrates” the bot by finding the dinosaur’s location at runtime.
    print("Open chrome://dino and place the browser where the game is visible.")
    print("Move your mouse cursor over the dino and press Enter.")
    input("Press Enter when the mouse is over the dino...")
    x, y = pyautogui.position()
    region = (x + OFFSET_X, y - OFFSET_Y, SCAN_WIDTH, SCAN_HEIGHT)
    print(f"Using scan region: {region}")
    return region

def obstacle_ahead(region): # this function takes a screenshot of the defined region and checks for dark pixels, which indicate obstacles.
    screenshot = pyautogui.screenshot(region=region)
    gray = ImageOps.grayscale(screenshot)
    pixels = gray.getdata()
    return any(pixel < THRESHOLD for pixel in pixels)

def jump(): # this function simulates a jump by pressing the spacebar.
    pyautogui.press("space")

def main(): # this is the main function that runs the bot. It calibrates the scan region, starts the game, and continuously checks for obstacles to jump over.
    scan_region = calibrate()
    print("Bot will start in 3 seconds. Switch to the game window.")
    time.sleep(3)

    # Start the game if it is not already running
    pyautogui.press("space")
    time.sleep(0.5)

    while True: # the main loop that keeps the bot running. It checks for obstacles and jumps when necessary.
        if obstacle_ahead(scan_region):
            jump()
            time.sleep(0.15)
        time.sleep(0.01)

if __name__ == "__main__":
    main()

# if you want to access into this game just run this code and write into your browser "brave://dino" (if you use chrome, write chrome instead) and start to play.