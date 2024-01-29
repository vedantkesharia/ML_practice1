#pylint:disable=no-member

# Masking in computer vision refers to the process of using a binary image (referred to as a mask) to selectively modify or analyze certain parts of another image. The binary mask acts as a filter, specifying which pixels or regions of the original image should be considered or excluded in subsequent operations.

import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/cats 2.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45,img.shape[0]//2), 100, 255, -1)

# rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

# weird_shape = cv.bitwise_and(circle,rectangle)
# cv.imshow('Weird Shape', weird_shape)

masked = cv.bitwise_and(img,img,mask=circle) 
# you can also try rectangle or weird shape in mask

cv.imshow('Weird Shaped Masked Image', masked)

cv.waitKey(0)
