import socket  # Import socket module
from os import stat

def interact(c):
    c.send("FILE_LIST")
    try:
        while True:
            # Receive Directory Details
            dir_details = ""
            try:
                while True:
                    msg = c.recv(1024)
                    if msg:
                        dir_details += msg
                        if msg[-1] == "/":
                            break
                    else:
                        break
            except KeyboardInterrupt:
                return
            #  Parse the received message
            lines = dir_details.split("\n")
            curr_directory = lines[0]
            i = 1
            folders = []
            files = []

            try:
                while True:
                    if lines[i] == "":
                        break
                    else:
                        folders.append(lines[i])
                    i += 1
            except KeyboardInterrupt:
                return
            i += 1
            try:
                while True:
                    if lines[i] == "/":
                        break
                    else:
                        files.append((lines[i], int(lines[i+1])))
                    i += 2
            except KeyboardInterrupt:
                return

            print curr_directory
            print folders
            print files
            GUI_DATA = {"Dir": curr_directory, "Folders":folders, "Files":files}
            # Take user input
            option = input("\nPlease enter your choice. 0 to Go back. -1 to exit\n\n")
            while option < -1 or option > len(folders) + len(files):
                print "Invalid Input\n\n"
                option = input("\nPlease enter your choice. 0 to Go back. -1 to exit\n\n")
            # Send the Choice to the server
            try:
                c.send(str(option))
            except KeyboardInterrupt:
                return
            # Enter receive mode if file is selected
            if option > len(folders):
                try:
                    receive_file(c, files[option - len(folders) - 1])
                except KeyboardInterrupt:
                    return
            # Disconnect if -1
            if option == -1:
                return
    except KeyboardInterrupt:
        return


def receive_file(c, (name, size)):
    print "Receiving File"
    received = 0
    # Create a file
    f = open(name, 'wb')
    try:
        while received < size:
            #  Receive in parts
            part = c.recv(1024)
            # Update the size received
            received += len(part)
            # Write part onto file
            f.write(part)
    except KeyboardInterrupt:
        f.close()
        raise KeyboardInterrupt
    # Close the file
    f.close()
    # Send ACK
    c.send("ACK")
    print "Received File"
    return


def connect_to_server(PORT = 12345, HOST = None):
    # cretate a socket
    try:
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print "Socket successfully created"
    except socket.error as err:
        print "*****socket creation failed with error %s*****" % err
        return

    # HOST = socket.gethostname()  # Get local machine name
    HOST = '127.0.0.1'

    # Try to connect to the server
    try:
        c.connect((HOST, PORT))
        print "Connected to server"
    except socket.error as err:
        print "*****Connection failed with error %s*****" % err
        return

    # Receive Message form server
    msg = c.recv(1024)

    if msg == "Connection successful":
        return c
    return


def download():
    c = connect_to_server()
    interact(c)
    c.close()


def send_file(c, filepath):
    print "Uploading file"
    msg = c.recv(1024)
    size = stat(filepath).st_size
    index = filepath.rfind('/')
    file_name = filepath[index+1:]
    if msg == "ACK":
        c.send(str(size))
        c.send("\n")
        c.send(file_name)
        c.send("\n")
        c.send("/")
    else:
        print "Upload unsuccessful"
        return
    msg = c.recv(1024)
    if msg != "ACK":
        print "Upload unsuccessful"
        return
    f = open(filepath,'rb')
    sent = 0
    while sent < size:
        part = f.read(1024)
        c.send(part)
        sent+=len(part)
    f.close()
    print "File Uploaded"
    return




def upload(filepath):
    c = connect_to_server()
    c.send("UPLOAD")
    send_file(c, filepath)
# host = socket.gethost
print socket.gethostname()
# download()
upload("/home/cselab210/Desktop/ES15BTECH11014/OS/kalloc.cpp")
