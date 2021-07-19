#!/usr/bin/env python3

from os import path, makedirs
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

# Check if arg is passed
try:
    projectname = argv[1]
except IndexError:
    # print("Usage: "+ path.basename(argv[0]) + " project_name")
    print("Please provide project name as second argument.")
    exit()

# Check if project exists
def check(directory, file):
    """ Function to check if project exists """

    if path.isfile(file) and path.isdir(directory):
        print("Project: '"+ projectname + "' already exist!")
        exit()
    else:
        # If not exist call functions
        conf(file, projectname)
        dir(directory)

        print("Project '"+ projectname +"' created!")

# Create directory
def dir(directory):
    """ Function to create documents root directory """

    if not path.exists(directory):
        makedirs(directory, exist_ok=True)

# Function to create nginx configuration file
def conf(file, projectname):
    """ Function to create nginx configuration file """

    tpl = """
server {{
    listen 80;
    server_name {name}.lc;
    root /opt/homebrew/var/www/{name}/public;

    client_max_body_size 256M;

    add_header X-Frame-Options "SAMEORIGIN";
    add_header X-Content-Type-Options "nosniff";

    index index.php;

    charset utf-8;

    location / {{
        try_files $uri $uri/ /index.php?$query_string;
    }}

    location = /favicon.ico {{ access_log off; log_not_found off; }}
    location = /robots.txt  {{ access_log off; log_not_found off; }}

    error_page 404 /index.php;

    location ~ \.php$ {{
        fastcgi_pass 127.0.0.1:9000;
        fastcgi_param SCRIPT_FILENAME $realpath_root$fastcgi_script_name;
        include fastcgi_params;
    }}

    location ~ /\.(?!well-known).* {{
        deny all;
    }}
}}
        """.format(name=projectname)
    try:
        f = open(file, "x")
        f.write(tpl)
        f.close()
    except FileExistsError:
        print("File: '"+ file + "' already exists!")
        exit()

if __name__== "__main__":
    check(brewhome +  '/var/www/' + projectname, brewhome + '/etc/nginx/servers/' + projectname + '.conf')
