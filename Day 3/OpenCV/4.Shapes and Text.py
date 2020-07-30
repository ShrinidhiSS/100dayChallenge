import cv2
import numpy as np


img = np.zeros((512,512,3),np.uint8)

cv2.line(img,(0,0),(512,512),(255,0,0),3)
cv2.rectangle(img,(200,300),(300,500),(0,0,255),cv2.FILLED)
cv2.circle(img,(400,350),23,(0,255,0),5)
cv2.putText(img," Open CV ",(100,100),cv2.FONT_HERSHEY_TRIPLEX,2,(255,0,0),2)

cv2.imshow("Image",img)

cv2.waitKey(0)