from os import listdir
from os.path import isfile, join
from os import stat
root = "/home/rahul/Desktop"
mypath = root
while True:
	folders = [f for f in listdir(mypath) if not isfile(join(mypath, f))]
	folders.sort()
	n1 = len(folders)

	files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	files.sort()
	n2 = len(files)
	print "\n*******************************\n"
	print ("Current Directory : %s" %mypath)
	i = 1
	print "\nFolders"
	for folder in folders:
		print i, folder
		i += 1

	print "\nFiles"
	for file in files:
		print i, file
		i += 1

	option = input("\nPlease enter your choice. 0 to Go back. -1 to exit\n\n")
	# while type(option) != int:
	# 	option = raw_input("Please enter your choice. 0 to Go back. -1 to exit\n")
	if option == -1:
		break
	if option == 0:
		if mypath==root:
			print "Cannot go back further"
			continue
		index = mypath.rfind('/')
		mypath = mypath[0:index]
	elif option >= n1:
		file_info = stat(join(mypath,files[option-n1-1]))
		print("You have selected %s" %files[option-n1-1])
		print ("File Size: %d bytes" %file_info.st_size)
		print "Enter 1 to send. Anything else to go back\n"
		option = input()
		if option == 1 :
			break
	else:
		mypath = join(mypath, folders[option-1])