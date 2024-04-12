import pyautogui
import time

def rdp_connect(server_name, password):
    # Open Remote Desktop Connection application
    pyautogui.press('winleft')
    pyautogui.typewrite('remote desktop connection')
    pyautogui.press('enter')
    
    # Wait for Remote Desktop Connection to open
    time.sleep(2)
    
    # Type the server name
    pyautogui.typewrite(server_name)
    pyautogui.press('enter')
    
    # Wait for the server connection window to open
    time.sleep(2)
    
    # Type the password
    pyautogui.typewrite(password)
    pyautogui.press('enter')

# Example usage
server_name = "example.server.com"
password = "your_password"
rdp_connect(server_name, password)
