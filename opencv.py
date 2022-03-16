#!/usr/local/bin/python3.10 

import cv2

img = cv2.imread('assets/ChubbyCat.png', cv2.IMREAD_COLOR)
#img = cv2.resize(img, (400,500))
read_Img = cv2.imread('assets/ChubbyCat.png', -1)
font = cv2.FONT_HERSHEY_SIMPLEX
font_size = 0.7
Blue_Color = (255,0,0)
org = (390,20)
text_thickness = 1
cv2.circle(img, (450,150), 125, (0,0,255), 2)
cv2.putText(img, 'Face Detected!',org, font, font_size, Blue_Color, text_thickness, cv2.LINE_AA, False)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#print(read_Img)
