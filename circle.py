import cv2
import numpy as np

picta=cv2.imread("kruh.jpg")

gray=cv2.cvtColor(picta,cv2.COLOR_BGR2GRAY)

thresh=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

im2,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

cv2.drawContours(picta,contours, -1, (0,255,0), 3)

cv2.imshow("test",picta)
cv2.waitKey(0)&0xFF
cv2.destroyAllWindows()
