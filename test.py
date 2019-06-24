import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

path = os.getcwd()
path = os.path.join(path,'images\P')

categories = ['cracks', 'nocracks']
#appending 500 images with cracks
pathcracks = os.path.join(path,'crackstrain')

files =  os.listdir(pathcracks)[0:500]
for f in files:
    imagepath = os.path.join(pathcracks,f)
    img = cv2.imread(imagepath)
    
    break
print(f)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
