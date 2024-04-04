import pexpect

def ssh_connect(hostname, username, password):
    # Spawn a new SSH session
    ssh_session = pexpect.spawn(f'ssh {username}@{hostname}')

    try:
        # Expect password prompt
        ssh_session.expect('password:')

        # Send the password
        ssh_session.sendline(password)

        # Now, you can interact with the server using ssh_session.sendline() to send commands

        # Example: sending a command to list files in the home directory
        ssh_session.sendline('ls ~')

        # Wait for the command to finish and print the output
        ssh_session.expect(pexpect.EOF)
        print(ssh_session.before)

    except pexpect.EOF:
        print("Connection closed unexpectedly")
    finally:
        # Close the SSH session
        ssh_session.close()

# Function to connect to multiple hosts
def connect_to_multiple_hosts(hostnames, username, password):
    for hostname in hostnames:
        print(f"Connecting to {hostname}...")
        ssh_connect(hostname, username, password)
        print("")

# Example usage
hostnames = ['host1.example.com', 'host2.example.com', 'host3.example.com']
username = 'your_username'
password = 'your_password'

connect_to_multiple_hosts(hostnames, username, password)
