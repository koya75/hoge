import cv2
import numpy as np

img=cv2.imread('black.png',1)

pts=np.array(((100,100),(300,100),(200,273)))
img1=cv2.fillPoly(img,[pts],(0,212,255))
pts1=np.array(((200,100),(150,186),(250,186)))
img2=cv2.fillPoly(img1,[pts1],(0,0,0))
img2=cv2.flip(img2,0)

cv2.imshow('Zeruda',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
