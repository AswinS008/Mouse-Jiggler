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
    ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    import subprocess as sp
import time
def open_putty(hostname):

	username="e5687265"	
	password="Natasaidhellov@1d"
	command= f'start putty {username}@{hostname}'

	sp.run(command, shell=True)

	#process= sp.Popen(command, stdin=sp.PIPE, shell=True)
	#time.sleep(1)
	#process.stdin.write(f"{password}\n".encode())
	#process.stdin.flush()
	
if __name__== "__main__":
	hostnames = ['10.18.102.29','10.18.102.30','10.18.102.51','10.18.102.27']
	for hostname in hostnames:
		open_putty(hostname)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  import subprocess

def ssh_connect(hostname, username, password):
    # Start PuTTY process
    command = ['putty.exe', f'{username}@{hostname}']

    try:
        # Open a subprocess and interact with it
        ssh_process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        # Send username
        ssh_process.stdin.write(username + '\n')
        ssh_process.stdin.flush()

        # Send password
        ssh_process.stdin.write(password + '\n')
        ssh_process.stdin.flush()

        # Now, you can interact with the server using ssh_process.stdin.write() to send commands

        # Example: sending a command to list files in the home directory
        ssh_process.stdin.write('ls ~\n')
        ssh_process.stdin.flush()

        # Print output
        output = ssh_process.stdout.read()
        print(output)

    except Exception as e:
        print("An error occurred:", e)
    finally:
        # Close the SSH session
        ssh_process.stdin.close()
        ssh_process.stdout.close()
        ssh_process.stderr.close()

# Function to connect to multiple hosts
def connect_to_multiple_hosts(hostnames, username, password):
    for hostname in hostnames:
        print(f"Connecting to {hostname}...")
        ssh_connect(hostname, username, password)
        print("")

# Example usage

hostnames = ["10.18.94.155","10.18.94.156"]
username = 'e5687265'
password = 'Natasaidhellov@1d'

connect_to_multiple_hosts(hostnames, username, password)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
