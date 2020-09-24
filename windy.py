## By Brandon Winston
## Script type: Everyday use
## Script to check file extention and move to relative directory
## Language: Python

import os
import os.path
from os import path

def main():
    global USER
    USER = os.environ.get('USER')


    file_types = [".exe",".aif",".cda",".mid",".mp3",".mpa",".wav",
                    ".sh",".deb",".java",".js",".html",".txt",".py"]
    directories = ["exe","aif","cda","mid","mp3","mpa","wav",
                    "sh","deb","java","js","html","txt","py"]

#    def try_create_directory():
        #for check in range(0,len(directories)):
        #    if not path.exists(directories[check]):
        #        make_directory = "mkdir /home/{}/Downloads/{}".format(USER,directories[check])
        #        os.system(make_directory)

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
                        command = "mv /home/{}/Downloads/{} ~/Downloads/exe".format(USER,file)
                        os.system(command)

    ## Function initilizations
    #try_create_directory()
    check_fileExtention()


if __name__ == "__main__":
    main()
