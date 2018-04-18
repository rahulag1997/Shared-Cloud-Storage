import socket               # Import socket module
import random
def interact(c):
	c.send("FILE_LIST")
	print "Request Sent"
	# while True:
	# curr_directory = c.recv(1024)
	# print curr_directory
	dir_details = ""
	while True:
		msg = c.recv(1024)
		if msg:
			# print msg
			dir_details += msg
			if msg[-1]=="/":
				break
		else:
			break
	# print dir_details
	lines = dir_details.split("\n")
	# print lines
	curr_directory = lines[0]
	i = 1
	folders = []
	files = []
	while True:
		if lines[i]=="": break
		else: folders.append(lines[i])
		i+=1
	i+=1
	while True:
		if lines[i]=="/": break
		else: files.append(lines[i])
		i+=1

	print curr_directory
	print folders
	print files

	option = input("\nPlease enter your choice. 0 to Go back. -1 to exit\n\n")
	while option<-1 or option > len(folders)+len(files):
		print "Invalid Input\n\n"
		option = input("\nPlease enter your choice. 0 to Go back. -1 to exit\n\n")
	c.send(str(option))

	if option ==-1:
		return

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
