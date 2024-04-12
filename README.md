import pyautogui
import time

def open_rdp():
    # Open Remote Desktop Connection application
    pyautogui.press('winleft')
    pyautogui.typewrite('remote desktop connection')
    pyautogui.press('enter')
    time.sleep(2)

def rdp_connect(server_name, password):
    # Type the server name
    pyautogui.typewrite(server_name)
    pyautogui.press('enter')
    
    # Wait for the server connection window to open
    time.sleep(2)
    
    # Type the password
    pyautogui.typewrite(password)
    pyautogui.press('enter')
    time.sleep(5)

# Example usage
def connect_to_servers(server_names, password):
    open_rdp()
    for server_name in server_names:
        rdp_connect(server_name, password)

server_names = ["server1.example.com", "server2.example.com", "server3.example.com"]
password = "your_password"
connect_to_servers(server_names, password)







import pyautogui
import time

def rdp_connect(server_names, password):
    # Open Remote Desktop Connection application
    pyautogui.press('winleft')
    pyautogui.typewrite('remote desktop connection')
    pyautogui.press('enter')
    
    # Wait for Remote Desktop Connection to open
    time.sleep(2)
    
    for server_name in server_names:
        # Type the server name
        pyautogui.typewrite(server_name)
        pyautogui.press('enter')
        
        # Wait for the server connection window to open
        time.sleep(2)
        
        # Type the password
        pyautogui.typewrite(password)
        pyautogui.press('enter')
        
        # Wait for the connection to be established
        time.sleep(5)

# Example usage
server_names = ["server1.example.com", "server2.example.com", "server3.example.com"]
password = "your_password"
rdp_connect(server_names, password)




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
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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

# List of server names
server_names = ["server1.example.com", "server2.example.com", "server3.example.com"]
password = "your_password"

# Connect to each server
for server_name in server_names:
    rdp_connect(server_name, password)
    time.sleep(5)  # Optional delay between connections
