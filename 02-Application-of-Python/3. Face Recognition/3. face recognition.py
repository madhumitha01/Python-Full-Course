import cv2 #pip install opencv-python


#Loading The Cascade File
face_cascade = cv2.CascadeClassifier(r"D:\PERSONAL\Python\Python-Full-Course\02-Application-of-Python\3. Face Recognition\haarcascade_frontalface_default.xml")

#Reading the Input Image
# image= cv2.imread('1.jpg')
image= cv2.imread(r"D:\PERSONAL\Python\Python-Full-Course\02-Application-of-Python\3. Face Recognition\1.png")

#Resizing the Image
img = cv2.resize(image,None,fx=0.3,fy=0.3)

#Converting the image into grayscale image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detecting The Faces
faces = face_cascade.detectMultiScale(imgGray, 1.2, 5)

#Pointing The Faces
for (x,y,w,h) in faces:
	cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)

#Displaying The Output Image
cv2.imshow('img', img)
cv2.waitKey()