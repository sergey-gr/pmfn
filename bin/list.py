#!/usr/bin/env python3

from os import listdir, path
from sys import argv, exit
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

def list(*args):
    """ Function to files in directoriy or multiple directories """

    for dir in args:
        if not path.isdir(dir):
            print("Project: '"+ projectname + "' does not exists!")
            exit()
        else:
            print('Content of ' + dir + ': ' + str(listdir(dir)))
            if args.index(dir) != len(args)-1:
                print()

# Check if arg is passed
try:
    projectname = argv[1]
except IndexError:
    list('/opt/homebrew/var/www/', '/opt/homebrew/etc/nginx/servers/')
    exit()

if __name__== "__main__":
    list('/opt/homebrew/var/www/' + projectname)
