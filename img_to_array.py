#!/usr/bin/env python3

import os
from os import listdir
from os.path import isfile, join
import cv2 
import json
import pickle

raw_data = {"data":[], "target":[]}
HOME = "/home/nisha/dataset"
for  _dir in os.listdir(HOME):
     
     onlyfiles = [HOME+"/"+_dir+"/"+f for f in listdir(HOME+"/"+_dir) if isfile(join(HOME+"/"+_dir, f))]
     for img in onlyfiles:
         im = cv2.imread(img)
         raw_data["data"].append(im)
         raw_data["target"].append(img.split("/")[-1].split(".")[0])

data={}
with open("font_raw_data.json","r") as f:

     data=json.load(f)
data["data"] = raw_data["data"]
data["target"] = raw_data["target"]

with open("font_raw_data.json","w") as f:

     json.dump(data,f)

