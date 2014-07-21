
"""
Created on Tue Jul 08 14:28:18 2014
@author: paulinkenbrandt
"""
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('C:\\Users\\PAULINKENBRANDT\\Documents\\GitHub\\Image_Analysis\\fox.jpg')
b,g,r = cv2.split(img)
img2 = cv2.merge([r,g,b])

color = ('b','g','r')
plt.subplot(2,1,1)

for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])

ax =plt.subplot(2,1,2)

plt.imshow(img2)

ax.axis('off')

plt.show()