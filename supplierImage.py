#!/usr/bin/env python3
import requests, os
# The URL to upload the images
url = "http://localhost/upload/"
# To get the username from environment variable
usr = os.getenv('usr')
img_directory = '/home/{}/supplier-data/images/'.format(usr)
files = os.listdir(img_directory)
# Parsing through all the images
for img_nm in files:
    if not img_nm.startswith('.') and 'jpeg' in img_nm:
        img_path = img_directory + img_nm
        # uploading jpeg files
        with open(img_path, 'rb') as opened:
            r = requests.post(url, files={'file': opened})