import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import WindowCapture

#wincap = WindowCapture('RuneScape')

img_rgb = cv.imread("pics/Test.png")
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('pics/EmptyInventory.png',0)
w, h = template.shape[::-1]

res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv.imwrite('res.png',img_rgb)