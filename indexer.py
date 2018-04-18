from os import listdir
from os.path import isfile, join
from os import stat


def indexer(root="/home/rahul/Desktop"):
	# Initialise path to root
	mypath = root
	while True:
		# get the list of the folders in the directory
		folders = [f for f in listdir(mypath) if not isfile(join(mypath, f))]
		# Sort them alphabetically
		folders.sort()
		# Save the number of folders obtained while indexing
		n1 = len(folders)

		# get the list of files in the directory
		files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
		# sort them alphabetically
		files.sort()
		# store the number of files obtained
		n2 = len(files)
		# Print the list of files and directories obatined
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
		# Get user choice as input
		option = input("\nPlease enter your choice. 0 to Go back. -1 to exit\n\n")
		# Exit condition
		if option == -1:
			return None
		# Go back condtiion
		if option == 0:
			if mypath==root:
				print "Cannot go back further"
				continue
			index = mypath.rfind('/')
			mypath = mypath[0:index]
		elif option > n1:
			file_info = stat(join(mypath,files[option-n1-1]))
			print("You have selected %s" %files[option-n1-1])
			print ("File Size: %d bytes" %file_info.st_size)
			print "Enter 1 to send. Anything else to go back\n"
			option = input()
			if option == 1 :
				return join(mypath,files[option-n1-1])
		else:
			mypath = join(mypath, folders[option-1])