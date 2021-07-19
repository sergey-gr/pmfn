#!/usr/bin/env python3

# from os import path, rmdir, remove
from os import path, remove
from sys import argv, exit
from shutil import rmtree
from platform import processor

# Checking CPU architecture and set correct brew path
if processor() == 'i386': # Intel Mac
    brewhome = '/usr/local'
elif processor() == 'arm': # ARM Mac
    brewhome = '/opt/homebrew'
else:
    print('Are you on Mac?')
    exit()

projectname = None

# Check if arg is passed
try:
    projectname = argv[1]
except IndexError:
    # print("Usage: "+ path.basename(argv[0]) + " project_name" )
    print("Please provide project name as second argument.")
    exit()

# Check if project exists
def check(directory, file):
    """ Function to check if project exists """

    if not path.isfile(file) and not path.isdir(directory):
        print("Project: '"+ projectname + "' does not exists!")
        exit()
    else:
        # If exist do actions
        try:
            remove(file)
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))

        try:
            # rmdir(directory)
            rmtree(directory)
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))

        print("Project '"+ projectname +"' deleted!")

if __name__== "__main__":
    check(brewhome + '/var/www/' + projectname, brewhome +  '/etc/nginx/servers/' + projectname + '.conf')
