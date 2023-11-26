import cv2
import numpy as np
import imutils

# define a video capture object
vid = cv2.VideoCapture(0)
  



while True:

    ret, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.rectangle(gray,(384,0),(510,128),(0,255,0),3)
    cv2.imshow('frame', gray)


    image = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Find contours and filter for cards using contour area
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    threshold_min_area = 400
    number_of_contours = 0
    for c in cnts:
        area = cv2.contourArea(c)
        if area > threshold_min_area:
            cv2.drawContours(image, [c], 0, (36,255,12), 3)
            number_of_contours += 1

    print("Contours detected:", number_of_contours)
    cv2.imshow('thresh', thresh)
    cv2.imshow('image', image)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break