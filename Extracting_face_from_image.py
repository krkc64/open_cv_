import os
import sys
import numpy as np
from PIL import Image
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
im = cv2.imread("image.jpg")
#im = Image.open(""+dirname+"/"+subdirname+"/"+filename)
#gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(im, 1.3, 5)
for (x,y,w,h) in faces:
    	img = cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
    	#roi_gray = gray[y:y+h, x:x+w]
    	roi_color = img[y:y+h, x:x+w]
	name = './' + str(1) + '.jpg'
	print ('Creating...' + name)
	cv2.imwrite(name, roi_color)
