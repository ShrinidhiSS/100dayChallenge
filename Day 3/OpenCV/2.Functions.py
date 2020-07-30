import cv2
import numpy as np


img = cv2.imread('Resources/mars.jpg')

kernel = np.ones((5,5),np.uint8)
print(kernel)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,70,70)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Gray image",imgGray)
cv2.imshow("Blur image",imgBlur)
cv2.imshow("Canny image",imgCanny)     # Detect edges
cv2.imshow("Dilation image",imgDialation)     # Dilate the edges(Thickening)
cv2.imshow("Eroded image",imgEroded)     # Thinning the edges or dilation of edges

cv2.waitKey(0)