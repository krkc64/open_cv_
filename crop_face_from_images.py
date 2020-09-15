import os
import sys
import numpy as np
from PIL import Image
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

path = "/home/snake/Desktop/ca"

i = 0

c = 0
label=np.ones((20000,),dtype = int)

p = 0

for dirname , dirnames , filenames in os. walk ( path ):
        for subdirname in dirnames :
            subject_path = os. path . join ( dirname , subdirname )
            for filename in os. listdir ( subject_path ):
		im = cv2.imread("/home/snake/Desktop/ca/kat1/"+filename)
		#im = Image.open(""+dirname+"/"+subdirname+"/"+filename)
		#gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(im, 1.3, 5)
		for (x,y,w,h) in faces:
    			img = cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
    			#roi_gray = gray[y:y+h, x:x+w]
    			roi_color = img[y:y+h, x:x+w]
			name = './input_r3/' + str(i) + '.jpg'
	 		print ('Creating...' + name)
	 		cv2.imwrite(name, roi_color)
			i +=1
   			
		#img = im.resize((200,200))
    		#gray = img.convert('L')
		#gray.save(""+'input_r'+"/"+filename, "JPEG")
		#c +=1
		#label[p] = i
		#p +=1
	    
	    		



print('no of files are', i)
