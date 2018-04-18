from Indexer import iaa

ret_val = iaa("/home")

if ret_val==None:
	print "No file selected\n"
elif ret_val == -1:
	print "Invalid Home directory\n"
elif ret_val!=None:
	print ret_val
