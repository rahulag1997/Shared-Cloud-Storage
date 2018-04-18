# Import The socket library
from Indexer import Indexer
import socket

def host_server(PORT=12345, LIMIT=1):
	# cretate a socket 
	try:
	    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	    print "Socket successfully created"
	except socket.error as err:
	    print "*****Socket creation failed with error %s*****" %(err)
	    return

	# Bind the socket to a port
	try:
		s.bind(('', PORT))        
		print "Socket binded to %s" %(PORT)
	except socket.error as err:
	    print "****Socket Bind failed with error %s*****" %(err)
	    return

	# Set socket on listening mode
	s.listen(LIMIT)
	print "Socket listening on port ",PORT

	while True:
		try:
			c, addr = s.accept()     # Establish connection with client.
			print 'Got connection from', addr
			c.send('Connection successful')
			interact(c)
			c.close()
		except KeyboardInterrupt:
			break

	s.close()

def interact(c):
	msg = c.recv(1024)
	if msg == "FILE_LIST":
		# while True:
		print "Request Received"
		indexer = Indexer(root)
		curr_directory, folders, files = indexer.get_dir_details()
		c.send(curr_directory+"\n")
		for item in folders:
			c.send(item+'\n')
		c.send("\n")
		for item in files:
			c.send(item[0]+'    '+str(item[1])+"\n")
		c.send("/")
		# c.close()
		print "SENT"
		choice = c.recv(1024)
		print choice
		if choice == "-1": return
		elif int(choice) <= len(folders): 
			indexer.make_choice(int(choice))
			curr_directory, folders, files = indexer.get_dir_details()
			print curr_directory

		else: 
			send_file(indexer.get_file_path(int(choice)))
		return
	return

def send_file(file_path):
	print "Request to send ",file_path



root="/home/rahul/Desktop/DL"
host_server()