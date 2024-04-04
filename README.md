Traceback (most recent call last):
  File "c:\Users\e5687265\Desktop\ON call servers login.py", line 11, in <module> 
    open_putty(username, hostname, password)
  File "c:\Users\e5687265\Desktop\ON call servers login.py", line 4, in open_putty
    child = pexpect.spawn(command)
            ^^^^^^^^^^^^^
AttributeError: module 'pexpect' has no attribute 'spawn'
