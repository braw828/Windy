def move_on():
	pass
	
def move_to_others():
	import os
	os.system("ls /home/{}/Downloads/ > tmp/move_on.etm".format(os.environ.get('USER')))
	open_fileEXTM = open('tmp/move_on.etm','r')
	lines = open_fileEXTM.readlines()
	count = 0
	for line in lines:
		file = format(line.strip())
		result = extention_check(file)
		if result in file_types:
			for fle in range(0,len(file_types)):
				return file_types[fle]

def downloads_folder(list,downloads_result):
	from os import system as bash_input
	import os.path as check_if_exists
	from os import environ as ENV
	if not check_if_exists.exists("/home/{}/Downloads/DownloadsFolder".format(ENV.get('USER'))):
			make_directory = "mkdir /home/{}/Downloads/DownloadsFolder".format(ENV.get('USER'))
			bash_input(make_directory)
	else:
		move_on()

	lines = downloads_result.readlines()
	count = 0
	for line in lines:
		file = format(line.strip())
		for itter in range(0,len(list)):
			if file in list[itter]:
				bash_input("mv /home/{}/Downloads/{} /home/{}/Downloads/DownloadsFolder".format(ENV.get('USER'),file,ENV.get('USER')))


def windyFiles():
	import os
	from locals.blueprint_variables import file_types,directories
	if not os.path.exists(f"/home/{os.environ.get('USER')}/WindyFiles"):
		os.system(f"mkdir ~/WindyFiles")
	if not os.path.exists(f"/home/{os.environ.get('USER')}/WindyFiles/DownloadsFolder"):
		os.system(f"mkdir ~/WindyFiles/DownloadsFolder")
	if not os.path.exists(f"/home/{os.environ.get('USER')}/WindyFiles/OtherFiles"):
		os.system(f"mkdir ~/WindyFiles/OtherFiles")
	else:move_on()

def windyFiles_content():
	import os
	from locals.blueprint_variables import file_types,directories
	for itter in range(0,len(directories)):
		if not os.path.exists(f"/home/{os.environ.get('USER')}/WindyFiles/DownloadsFolder/{directories[itter]}"):
			os.system(f"mkdir ~/WindyFiles/DownloadsFolder/{directories[itter]}")
		else:move_on()
