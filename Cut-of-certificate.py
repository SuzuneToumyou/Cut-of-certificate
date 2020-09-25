#!/usr/bin/python3 #環境によって変えてくださいね
# -*- coding: utf-8 -*

import cv2
import numpy as np

fname="input.jpg"
threshold=220 

img_color= cv2.imread(fname) 
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
img_blur = cv2.blur(img_gray,(9,9))

ret, img_binary= cv2.threshold(img_blur, threshold, 255, cv2.THRESH_BINARY_INV) 

contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

rect = cv2.minAreaRect(contours[0])
box = cv2.boxPoints(rect)
box = np.int0(box)

height = int(np.sqrt(np.abs(box[3][0]-box[2][0])*(np.abs(box[2][1]-box[3][1]))))
width = int(np.sqrt(np.abs(box[2][0]-box[1][0])*(np.abs(box[1][1]-box[2][1]))))

center = (height, width)

angle = rect[2]
scale = 1.0
trans = cv2.getRotationMatrix2D(center, angle , scale)

img2 = cv2.warpAffine(img_color, trans, (0,0),borderValue=(255, 255, 255))#背景白のとき
#img2 = cv2.warpAffine(img_color, trans, (0,0),borderValue=(0,0,0))#背景黒のとき

img_color= img2
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
img_blur = cv2.blur(img_gray,(9,9))

ret, img_binary= cv2.threshold(img_blur, threshold, 255, cv2.THRESH_BINARY_INV) 

contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 

rect = cv2.minAreaRect(contours[0])
box = cv2.boxPoints(rect)
box = np.int0(box)

img3 = img2[box[2][1]:box[0][1],box[1][0]:box[0][0]]
cv2.imwrite("output.jpg", img3)

print("Completed!")
