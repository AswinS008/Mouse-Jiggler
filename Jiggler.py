import pyautogui
import time

def jiggle_mouse():
    try:
        while True:
            # Move the mouse by 1 pixel in both x and y directions
            pyautogui.move(1, 1)
            pyautogui.move(-1, -1)
            time.sleep(1)  # Wait for 5 seconds before next movement
    except KeyboardInterrupt:
        print("Mouse jiggling stopped.")

if __name__ == "__main__":
    jiggle_mouse()
