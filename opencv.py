#!/usr/local/bin/python3.10 
# importing library
import cv2

# assigning var's to cv2 fxns
img = cv2.imread('assets/ChubbyCat.png', cv2.IMREAD_COLOR)
read_Img = cv2.imread('assets/ChubbyCat.png', -1)
font = cv2.FONT_HERSHEY_SIMPLEX

# assiging vars to numbers in case of neatness
font_size = 0.7
Blue_Color = (255,0,0)
org = (390,20)
text_thickness = 1

#cv2 fxns
cv2.circle(img, (450,150), 125, (0,0,255), 2) #adding circle
cv2.putText(img, 'Face Detected!',org, font, font_size, Blue_Color, text_thickness, cv2.LINE_AA, False) #adding text
cv2.imshow('img', img) # showing image in a window
cv2.waitKey(0) # indefinite wait key so the image doesn't disappear in an instant when ran 
cv2.destroyAllWindows() # press any key while on image to remove window from screen

