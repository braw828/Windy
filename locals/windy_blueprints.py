

def move_on():
	pass



def add_directory_DOWNLOADS_F(*args):

	if args:
		import os
		for arg in args:
			try:
				directory = arg
				parent_dir = "/home/{}/Downloads/".format(os.environ.get('USER'))
				path = os.path.join(parent_dir,directory)
				os.mkdir(path)
			except FileExistsError:
				move_on()
	else:
		print("Add directory name")
def create_others():
	import os
	import os.path
	if not os.path.exists("/home/{}/Downloads/OtherFiles".format(os.environ.get('USER'))):
		add_directory_DOWNLOADS_F("OtherFiles")
	else:
		move_on()
#def move_to_others():
