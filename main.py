import socket
import subprocess
import sys
import os
from datetime import datetime

subprocess.call('cls' if os.name == "nt" else "clear", shell=True)

remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

print ("_" * 60)
print ("Please wait, scanning remote host", remoteServerIP)
print ("_" * 60)

t1 = datetime.now()

try: 
    for port in range(1,5000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.05)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("Port {}: Open".format(port))
        sock.close()
except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
except socket.error:
    print("Couldn't connect to server")

t2 = datetime.now()
total = t2 - t1
print("Scanning Completed in : ", total)