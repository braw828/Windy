## By Brandon Winston
## Script type: Everyday use
## Script to check file extention and move to relative directory
## Language: Python
import os
import shutil
import os.path
from os import path
import locals.windy_blueprints
from locals.windy_blueprints import (move_on,
downloads_folder,windyFiles,windyFiles_content)

def windy():
    global USER
    USER = os.environ.get('USER')

    download_status = ".part"
    file_types = [".exe",".aif",".cda",".mid",".mp3",".mpa",".wav",
                    ".sh",".deb",".java",".js",".html",".txt",".py",".bin"]
    directories = ["exe","aif","cda","mid","mp3","mpa","wav",
                    "sh","deb","java","js","html","txt","py","bin"]



    def extention_check(file):
            extention = os.path.splitext("/home/{}/Downloads/{}".format(USER,file))
            file_ext = extention[1]
            return file_ext


    ## Funtion to check file extention
    def check_fileExtention():
        ## Shell execution
        USER = os.environ.get('USER')
        command = "ls /home/{}/Downloads/ > tmp/files.etm".format(USER)
        os.system(command)
        ## Reading lines from "files.etm"
        open_fileEXTM = open('tmp/files.etm','r')
        lines = open_fileEXTM.readlines()
        count = 0
        ## Striping new line character
        for line in lines:
            file = format(line.strip())
            result = extention_check(file)
            if result in file_types:
                for fle in range(0,len(file_types)):
                    if result in file_types[fle]:
                        command = "mv /home/{}/Downloads/'{}' ~/WindyFiles/DownloadsFolder/{}".format(USER,file,result[1:])
                        os.system(command)

    def move_to_others():
    	import os
    	os.system("ls /home/{}/Downloads/ > tmp/move_on.etm".format(os.environ.get('USER')))
    	open_fileEXTM = open('tmp/move_on.etm','r')
    	lines = open_fileEXTM.readlines()
    	count = 0
    	for line in lines:
            file = format(line.strip())
            if file not in directories:

                if not os.path.exists(f"/home/{os.environ.get('USER')}/WindyFiles/OtherFiles/{file}"):
                    os.system(f"mv ~/Downloads/'{file}'  ~/WindyFiles/OtherFiles/")

                else:
                    os.system(f"rm -rf /home/{os.environ.get('USER')}/Downloads/'{file}'")
                    move_on()




    ## Function initilizations
    windyFiles()
    windyFiles_content()
    check_fileExtention()
    move_to_others()



if __name__ == "__main__":
    windy()
