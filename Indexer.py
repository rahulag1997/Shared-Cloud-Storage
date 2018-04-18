from os import listdir
from os.path import isfile, join, exists
from os import stat

class Indexer:
	def __init__(self, r):
		self.root = r
		self.mypath = r

	def get_dir_details(self):
		# get the list of the folders in the directory
		self.folders = [f for f in listdir(self.mypath) if not isfile(join(self.mypath, f))]
		# Sort them alphabetically
		self.folders.sort()
		# Save the number of folders obtained while indexing
		self.n1 = len(self.folders)

		# get the list of files in the directory
		files = [f for f in listdir(self.mypath) if isfile(join(self.mypath, f))]
		# sort them alphabetically
		files.sort()

		# store the number of files obtained
		self.n2 = len(files)

		# Extract Details
		self.file_details = []
		for file in files:
			file_info = stat(join(self.mypath,file))
			self.file_details.append([file, file_info.st_size])

		return self.mypath, self.folders, self.file_details

	def make_choice(self, choice):
		if option == 0:
			if self.mypath==self.root:
				return
			index = self.mypath.rfind('/')
			self.mypath = self.mypath[0:index]
		else:
			self.mypath = join(self.mypath, self.folders[choice-1])

	def get_file_path(self, choice):
		return join(self.mypath,self.file_details[choice-self.n1][0])








def iaa(root="/home/rahul/Desktop"):
	# Initialise path to root
	mypath = root
	if not exists(root):
		return -1
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