import pexpect
import subprocess as sp

def ssh_connect(hostname, username, password):
    # Spawn a new SSH session
    command= f'start putty {username}@{hostname}'
    sp.run(command, shell=True)

    try:
        # Send the password
        command.sendline(password)

        # Now, you can interact with the server using ssh_session.sendline() to send commands

        # Example: sending a command to list files in the home directory
        command.sendline('ls ~')

        # Wait for the command to finish and print the output
        command.expect(pexpect.EOF)
        print(command.before)

    except pexpect.EOF:
        print("Connection closed unexpectedly")
    finally:
        # Close the SSH session
        command.close()

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












During handling of the above exception, another exception occurred:       

Traceback (most recent call last):
  File "c:\Users\e5687265\Desktop\on call new.py", line 40, in <module>   
    connect_to_multiple_hosts(hostnames, username, password)
  File "c:\Users\e5687265\Desktop\on call new.py", line 32, in connect_to_multiple_hosts
    ssh_connect(hostname, username, password)
  File "c:\Users\e5687265\Desktop\on call new.py", line 26, in ssh_connect
    command.close()
    ^^^^^^^^^^^^^
AttributeError: 'str' object has no attribute 'close'
