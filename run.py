#!/usr/bin/env python3

import os, requests, json

def catalog_data(url,des_dir):
    """This function will return a list of dictionaries with all the details like name, weight, des, image_name.
    It will change the weight to integer format.
    """
    fruit={}
    for item in os.listdir(des_dir):
      fruit.clear()
      filename=os.path.join(des_dir,item)
      with open(filename) as f:
        line=f.readlines()
        des=""
        for i in range(2,len(line)):
          des=des+line[i].strip('\n').replace(u'\xa0',u'')
        fruit["description"]=des
        fruit["weight"]=int(line[1].strip('\n').strip('lbs'))
        fruit["name"]=line[0].strip('\n')
        fruit["image_name"]=(item.strip('.txt'))+'.jpeg'
        print(fruit)
        if url!="":
          response=requests.post(url, json=fruit)
          print(response.request.url)
          print(response.status_code)
    return 0
        
if __name__=='__main__':
    url = 'http://localhost/fruits/'
    usr = os.getenv('usr')
    des_directory = '/home/{}/supplier-data/dess/'.format(usr)
    catalog_data(url,des_directory)