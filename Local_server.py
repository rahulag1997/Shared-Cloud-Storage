# Import The socket library
from Indexer import Indexer
import socket


def host_server(PORT = 12345, LIMIT = 1):
    # create a socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print "Socket successfully created"
    except socket.error as err:
        print "*****Socket creation failed with error %s*****" % err
        return

    # Bind the socket to a port
    try:
        s.bind(('', PORT))
        print "Socket binded to %s" % PORT
    except socket.error as err:
        print "****Socket Bind failed with error %s*****" % err
        return

    # Set socket on listening mode
    s.listen(LIMIT)
    print "Socket listening on port ", PORT

    while True:
        try:
            c, addr = s.accept()  # Establish connection with client.
            print 'Got connection from', addr
            c.send('Connection successful')
            interact(c)
            c.close()
            print "Disconnected Form client",addr
        except KeyboardInterrupt:
            break

    s.close()


def interact(c):
    msg = c.recv(1024)
    if msg == "FILE_LIST":
        # Create a indexer object
        indexer = Indexer(root)
        while True:
            #  Get Directory details
            curr_directory, folders, files = indexer.get_dir_details()
            print "Current Directory :",curr_directory
            #  Send the details to the client

            c.send(curr_directory + "\n")
            for item in folders:
                c.send(item + '\n')
            c.send("\n")
            for item in files:
                c.send(item[0] + '\n' + str(item[1]) + "\n")
            c.send("/")
            # Receive response from client
            choice = c.recv(1024)

            # Is -1 disconnect
            if choice == "-1":
                print "Disconnecting from Client"
                return
            elif int(choice) <= len(folders):  # Change directory if folder is selected
                indexer.make_choice(int(choice))
            else:
                send_file(c, indexer.get_file_path(int(choice))) #Send file if file is selected
    return


def send_file(c, file_path):
    print "Request to send ", file_path
    print "Sending File "
    # Open File
    f = open(file_path,'rb')
    # Read file in parts
    part = f.read(1024)
    while part:
        # Send part
        c.send(part)
        part = f.read(1024)
    # Wait for confirmation from client
    msg = c.recv(1024)
    if(msg=="ACK"):
        print "Send successful"
    else:
        print "Send unsuccessful"



root = "/home/cselab210/Desktop/ES15BTECH11014"
host_server()
