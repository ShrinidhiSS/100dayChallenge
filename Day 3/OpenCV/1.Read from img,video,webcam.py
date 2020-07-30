#Read image, video, webcam

import cv2
print("Package imported")


# Read image
img = cv2.imread('Resources/mars.jpg')

cv2.imshow("Output",img)
cv2.waitKey(0)



# Read video
# cap = cv2.VideoCapture('Resources/mouse.mp4')
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break



# Read webcam
# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# cap.set(10,500)
#
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


