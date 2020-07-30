import cv2

img = cv2.imread('Resources/mars.jpg')
print(img.shape)

imgResize = cv2.resize(img,(600,300))
print(imgResize.shape)

# Cropping
imgCropped = img[0:400,600:900]

cv2.imshow("Img",img)
cv2.imshow("Resize img",imgResize)
cv2.imshow("Cropped img",imgCropped)
cv2.waitKey(0)