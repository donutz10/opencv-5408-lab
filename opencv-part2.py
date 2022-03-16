#!/usr/local/bin/python3.10 

#part 2 of lab 6
#library imports
import numpy as np
import cv2
from matplotlib import pyplot as plt


#assigning var's to cv2 functions to read, canny and blur desired image
img = cv2.imread('assets/ChubbyCat.png', cv2.IMREAD_GRAYSCALE)
img_edges = cv2.Canny(img,100,100)
img_edges_blur = cv2.GaussianBlur(img_edges, (7,7), cv2.BORDER_DEFAULT)



#plotting the image
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Gray Scale Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_edges_blur,cmap = 'gray') #change img_edges_blur to img_edges to view non blurred version 
plt.title('Edge Image with blur'), plt.xticks([]), plt.yticks([])
plt.show()


#cv2.waitKey(0)
#cv2.destroyAllWindows()

