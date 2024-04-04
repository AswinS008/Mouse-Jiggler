AttributeError: module 'pexpect' has no attribute 'spawn'
PS C:\Users\e5687265\Desktop> & C:/FIS/Python/python.exe "c:/Users/e5687265/Desktop/on call new.py"
Connecting to 10.18.94.155...
Traceback (most recent call last):
  File "c:\Users\e5687265\Desktop\on call new.py", line 40, in <module>
    connect_to_multiple_hosts(hostnames, username, password)
  File "c:\Users\e5687265\Desktop\on call new.py", line 32, in connect_to_multiple_hosts
    ssh_connect(hostname, username, password)
  File "c:\Users\e5687265\Desktop\on call new.py", line 5, in ssh_connect
    ssh_session = pexpect.spawn(f'ssh {username}@{hostname}')
                  ^^^^^^^^^^^^^
AttributeError: module 'pexpect' has no attribute 'spawn
