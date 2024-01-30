#pylint:disable=no-member

#Face detection -> classification (ie classiefies whether face present or not)

# haarcascade refers to Haar Cascade Classifiers, a machine learning object detection method used for identifying objects or faces in images or video streams. It is particularly popular for face detection. The term "Haar" comes from Haar wavelets, a mathematical concept used in the detection process.

# A Haar Cascade is trained from positive and negative images. Positive images contain the object of interest, while negative images do not. The training process involves extracting features from these images using Haar-like features, which are simple rectangular filters. The classifier then learns to distinguish between the positive and negative examples based on these features.

# Once trained, the Haar Cascade can be used to detect the object in new images or video frames efficiently. OpenCV, a popular computer vision library, provides pre-trained Haar Cascade models for various objects, including faces.

# For example, if you want to perform face detection using OpenCV in Python, you might use the cv2.CascadeClassifier class with the path to a pre-trained face detection Haar Cascade XML file.



import cv2 as cv

img = cv.imread('../Resources/Photos/group 1.jpg')
cv.imshow('Group of 5 people', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray People', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2) #drawing rectangle on face

cv.imshow('Detected Faces', img)



cv.waitKey(0)


#NOTES

# scaleFactor:

# scaleFactor compensates for the fact that a face closer to the camera will appear larger than a face that is farther away. It specifies how much the image size is reduced at each image scale.
# A smaller scaleFactor will increase the detection time but will increase the chance of detecting faces, especially small ones.
# Typical values for scaleFactor are between 1.01 and 1.3. A value of 1.1 means that the image is reduced in size by 10% at each image scale.


# minNeighbors:

# minNeighbors is a parameter specifying how many neighbors each candidate rectangle should have to retain it.
# This parameter helps filter out false positives. A higher minNeighbors value will require a higher number of overlapping rectangles to classify an area as a face. This can help reduce false positives but may also result in missing some true positives.
# Increasing minNeighbors tends to yield more reliable results but might miss some faces, while decreasing it may increase the number of false positives.