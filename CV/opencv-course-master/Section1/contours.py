#pylint:disable=no-member


# Contours in an image refer to the outlines or boundaries of objects or shapes present in that image. These outlines are formed by connecting points along the boundary of an object with lines, creating a curve that represents the shape. In image processing and computer vision, extracting contours can be a crucial step in various applications such as object recognition, shape analysis, and image segmentation.

# Contours can be used to identify and locate objects within an image, and they are particularly useful when dealing with binary or grayscale images. In a binary image, contours often represent the boundaries between regions of pixels with different intensity values.

# The process of finding contours typically involves edge detection, which highlights significant changes in intensity or color within the image. Once the edges are detected, contours can be extracted by connecting the points along these edges.




import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)