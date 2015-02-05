
"""
Created on Tue Jul 08 14:28:18 2014
@author: paulinkenbrandt
"""
import cv2
from matplotlib import pyplot as plt

#img = cv2.imread('C:\\Users\\PAULINKENBRANDT\\Documents\\GitHub\\Image_Analysis\\DSC_0723.png')
img = cv2.imread('C:/Users/PAULINKENBRANDT/Pictures/iCloud Photos/My Photo Stream/IMG_0495.jpg')
#b,g,r = cv2.split(img)
#img = cv2.merge([r,g,b])
img = img[:,:,::-1]
color = ('r','g','b')
plt.subplot(2,1,1)

for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])

ax =plt.subplot(2,1,2)

plt.imshow(img)

ax.axis('off')

plt.show()