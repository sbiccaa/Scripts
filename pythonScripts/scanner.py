#!/bin/python3


import sys # allows coomand line arguments and other stuff
import socket
from datetime import datetime

# Define the target 
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) # translat host to IPV4
else:
	print("invalid argument")
	print("syntax: python3 scanner.py <ip>")
	sys.exit()


#Add a pretty Banner 

print("-" * 50)
print("scanner.target "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)


try: 
	for port in range(50,80):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1) # float
		result = s.connect_ex((target,port))# error indicator
		if result == 0:
			print("Port {} is open".format(port))
		s.close()
			
except KeyboardInterupt:
	print("\nExiting Script. ")
	sys.exit()
	
except socket.gaierror:
	print("cannot resolve host. ")
	sys.exit()

except sockeet.error:
	print("Cannot connect to server. ")
	sys.exit()
	
	
