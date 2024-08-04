#Calcular el aspect ratio de una imagen

import cv2

im=cv2.imread("prueba.jpeg")

h,w,c=im.shape

ar=w/h

print("AspectRatioes:",ar) 