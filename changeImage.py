#!/usr/bin/env python3

import os
import sys
from PIL import Image #Pillow package for image transformations

usr = os.getenv('USER')
img_dir = '/home/{}/supplier-data/images/'.format(usr)
for img_nm in os.listdir(img_dir):
    if not img_nm.startswith('.') and 'tiff' in img_nm:
        img_path = img_dir + img_nm
        path = os.path.splitext(img_path)[0]
        #Image conversion
        im = Image.open(img_path)
        im.convert('RGB').resize((600, 400)).save(path+'.jpeg', "JPEG")