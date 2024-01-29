#pylint:disable=no-member

import cv2 as cv

# Read in an image
img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)

# # Converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# # Blur 
# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT) 
# cv.imshow('Blur', blur)

#(image,kernel_size(has to be an odd number so we take 7,7, higher the number more the blur),cv.BORDER_DEFAULT)


# # Edge Cascade -> trying to find the edges that are present in the image

# canny = cv.Canny(img, 125, 175) #(image,threholds)
# cv.imshow('Canny Edges', canny)

#we can reduce the number of edges by applying it on blurred image

# canny = cv.Canny(blur, 125, 175) #(image,threholds)
# cv.imshow('Canny Edges', canny)


# # Dilating the image
# dilated = cv.dilate(canny, (7,7), iterations=3)
# cv.imshow('Dilated', dilated)

# # Eroding
# eroded = cv.erode(dilated, (7,7), iterations=3)
# cv.imshow('Eroded', eroded)

# # Resize
# resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)

# # Cropping
# cropped = img[50:200, 200:400]
# cv.imshow('Cropped', cropped)

cv.waitKey(0)