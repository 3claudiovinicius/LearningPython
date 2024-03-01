#
# Example file for working with filesystem shell methods
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    # make a duplicate of an existing file
    #myfile = open("textfile.txt","w+")
    #myfile.close()
    if path.exists("textfile.txt"):
        # get the path to the file in the current directory
        src = path.realpath("textfile.txt")
        # let's make a backup copy by appending "bak" to the name
        dsb = src + ".bak"
        print(dsb)
        # rename the original file
        # shutil.copy(src,dsb)
        # now put things into a ZIP archive
        #os.rename("textfile.txt","newfile.txt")
        # more fine-grained control over ZIP files
        root_dir, tail = path.split(dsb)
        root_dir2, tail2 = path.split(src)
        #shutil.make_archive("zippedfile","zip",root_dir)
        with ZipFile("zippedfile.zip","w") as newzip:
            newzip.write(tail)
            newzip.write(tail2)

      
if __name__ == "__main__":
    main()
