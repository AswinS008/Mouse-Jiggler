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
hostnames = ["10.155", "10.156"]
username = 'e55'
password = 'N'

connect_to_multiple_hosts(hostnames, username, password)
