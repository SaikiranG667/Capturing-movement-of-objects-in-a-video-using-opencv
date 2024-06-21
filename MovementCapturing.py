import cv2
import numpy as np

cap=cv2.VideoCapture('example.mp4')
ret,frame1=cap.read()
ret,frame2=cap.read()
kernal=np.ones((10,10),np.uint8)
while(cap.isOpened()):

  diff=cv2.absdiff(frame1,frame2)
  gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
  blur=cv2.GaussianBlur(gray,(5,5),0)
  _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
  dilated=cv2.dilate(thresh,kernal,iterations=5)
  cv2.imshow('image2',dilated)
  contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

  # cv2.drawContours(frame1,contours,-1,(0,255,0),3)
  for i in contours:
    (x,y,w,h)=cv2.boundingRect(i)
    c=int(cv2.contourArea(i))
    if c>5000 & c<7000: #set the area of the rectangle which you want to capture on the video
      cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),3)
    
  cv2.imshow('video',frame1)
  frame1=frame2
  ret,frame2=cap.read()
  if(cv2.waitKey(1) & 0xFF ==27):
    break
cap.release()
cv2.destroyAllWindows()
