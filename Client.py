import socket  # Import socket module
import random


def interact(c):
    c.send("FILE_LIST")
    while True:
        # Receive Directory Details
        dir_details = ""
        while True:
            msg = c.recv(1024)
            if msg:
                dir_details += msg
                if msg[-1] == "/":
                    break
            else:
                break
        #  Parse the received message
        lines = dir_details.split("\n")
        curr_directory = lines[0]
        i = 1
        folders = []
        files = []
        while True:
            if lines[i] == "":
                break
            else:
                folders.append(lines[i])
            i += 1
        i += 1
        while True:
            if lines[i] == "/":
                break
            else:
                files.append((lines[i],int(lines[i+1])))
            i += 2

        print curr_directory
        print folders
        print files
        # Take user input
        option = input("\nPlease enter your choice. 0 to Go back. -1 to exit\n\n")
        while option < -1 or option > len(folders) + len(files):
            print "Invalid Input\n\n"
            option = input("\nPlease enter your choice. 0 to Go back. -1 to exit\n\n")
        # Send the Choice to the server
        c.send(str(option))
        # Enter receive mode if file is selected
        if option>len(folders):
            receive_file(c, files[option-len(folders)-1])
        # Disconnect if -1
        if option == -1:
            return

def receive_file(c, (name, size)):
    print "Receiving File"
    received = 0
    # Create a file
    f = open(name, 'wb')
    while received<size:
        #  Receive in parts
        part = c.recv(1024)
        # Update the size received
        received+=len(part)
        # Write part onto file
        f.write(part)
    # Close the file
    f.close()
    # Send ACK
    c.send("ACK")
    print "Received File"


def connect_to_server(PORT=12345, HOST=None):
    # cretate a socket
    try:
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print "Socket successfully created"
    except socket.error as err:
        print "*****socket creation failed with error %s*****" % (err)
        return

    # HOST = socket.gethostname()  # Get local machine name
    HOST = '127.0.0.1'

    # Try to connect to the server
    try:
        c.connect((HOST, PORT))
        print "Connected to server"
    except socket.error as err:
        print "*****Connection failed with error %s*****" % (err)
        return

    # Receive Message form server
    msg = c.recv(1024)

    if msg == "Connection successful":
        interact(c)

    # Close Socket
    c.close
    return


# host = socket.gethost
print socket.gethostname()
connect_to_server()
