import socket
import subprocess
import sys
import os
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

subprocess.call('cls' if os.name == "nt" else "clear", shell=True)

remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

print ("_" * 60)
print ("Please wait, scanning remote host", remoteServerIP)
print ("_" * 60)

t1 = datetime.now()

def scan(port): 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.2)
        start = datetime.now()
        result = sock.connect_ex((remoteServerIP, port))
        end = datetime.now()
        latency = (end - start).total_seconds() * 1000
        if result == 0:
            print (f"Port {port}: Open ({latency} ms)")
        sock.close()
        
try:
    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(scan, range(1, 5000)) 
            
except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
except socket.error:
    print("Couldn't connect to server")

t4 = datetime.now()
total = t4 - t1
print("Scanning Completed in : ", total)
