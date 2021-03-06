
import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('messi5.jpg')
imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread('messi5_face.jpg', 0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(imggray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0,255,0), 2)

cv2.imshow('img', img)
cv2.imshow('template', template)
cv2.waitKey(0)
cv2.destroyAllWindows()




