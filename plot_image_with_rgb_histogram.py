# -*- coding: utf-8 -*-
"""
Created on Tue Jul 08 14:28:18 2014

@author: paulinkenbrandt
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:\\Users\\PAULINKENBRANDT\\Documents\\GitHub\\Image_Analysis\\fox.jpg')

color = ('b','g','r')
plt.subplot(2,1,1)

for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])

ax =plt.subplot(2,1,2)

plt.imshow(img)

ax.axis('off')

plt.show()