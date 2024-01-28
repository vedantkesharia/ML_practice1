#pylint:disable=no-member

import cv2 as cv

# img = cv.imread('../Resources/Photos/cats.jpg')
# cv.imshow('Cats', img)   #(name you want to give, varible where it is stored)

# cv.waitKey(0)

# Reading Videos
capture = cv.VideoCapture('../Resources/Videos/dog.mp4') #(use number 0 in bracket like cv.VideoCapture(0) if you want to use webcam)


#we read a video frame by frame by using a loop
while True:
    isTrue, frame = capture.read()
    
    # if cv.waitKey(20) & 0xFF==ord('d'):
    # This is the preferred way - if `isTrue` is false (the frame could 
    # not be read, or we're at the end of the video), we immediately
    # break from the loop. 
    if isTrue:    
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()
