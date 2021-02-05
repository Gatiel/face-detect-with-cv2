import numpy as np
import cv2


face_cascade = cv2.CascadeClassifier('C:/Users/YOUR_USER/workspace/haarcascade_frontalface_default.xml') #change the directory to the folder where "haarcascade_frontalface_default.xml" is located

img = cv2.imread('#HERE#', cv2.IMREAD_UNCHANGED ) #place the image directory on "HERE"

scale_percent = 60 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(resized, (x, y), (x+w, y+h), (255, 0 ,0), 2)
    
cv2.imshow('img', resized)
cv2.waitKey()