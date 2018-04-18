import socket               # Import socket module
import random
def interact(c):
	c.send("FILE_LIST")
	# while True:
	# curr_directory = c.recv(1024)
	# print curr_directory
	i = 0
	dir_details = ""
	while True:
		msg = c.recv(1024)
		i+=1
		if msg:
			print msg
			dir_details += msg
		else:
			break
	print i
	lines = dir_details.split("\n")
	print lines


	# n1 = 0
	# msg = c.recv(1024)
	# while msg!="/":
	# 	print msg
	# 	msg = c.recv(1024)
	# 	n1+=1

	# msg = c.recv(1024)
	# while msg!= "/" and msg !="":
	# 	print msg,
	# 	size = c.rev(1024)
	# 	print size
	# 	msg = c.recv(1024)

	# option = input("\nPlease enter your choice. 0 to Go back. -1 to exit\n\n")
	# c.send(option)

	# if option ==-1:
	# 	return

def connect_to_server(PORT=12345, HOST=None):
	# cretate a socket 
	try:
	    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	    print "Socket successfully created"
	except socket.error as err:
	    print "*****socket creation failed with error %s*****" %(err)
	    return

	HOST = socket.gethostname() # Get local machine name


	# Try to connect to the server
	try:
		c.connect((HOST, PORT))
		print "Connected to server"
	except socket.error as err:
		print "*****Connection failed with error %s*****" %(err)
		return

	# Receive Message form server
	msg = c.recv(1024)

	if msg == "Connection successful":
		interact(c)

	# Close Socket
	c.close
	return






# host = socket.gethost
connect_to_server()
