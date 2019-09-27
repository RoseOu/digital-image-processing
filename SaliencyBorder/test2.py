#coding:utf-8

import numpy
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('11.png',0)
img = cv2.medianBlur(img,5)

# adaptive ------
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,2)

th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)

#----------
# Otsu's thresholding
# ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY) # Otsu's thresholding
# ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# blur = cv2.GaussianBlur(img,(5,5),0)
# ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#----------


titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

cv2.imwrite('11out.png', th3)


x,y,w,h=cv2.boundingRect(th3)
x=int(x)
y=int(y)
w=int(w)
h=int(h)

print(x,y,w,h)

imgth1 = cv2.imread('11out.png')
img2 = cv2.rectangle(imgth1,(x,y),(x+w,y+h),(255,255,255),1)
cv2.imwrite('11out1.png', img2)

origin_img = cv2.imread("1.jpg")
cropped = origin_img[y:y+h, x:x+w]  # 裁剪坐标为[y0:y1, x0:x1]
cv2.imwrite("1o.jpg", cropped)



#————————see------------
# for i in range(4):
#     plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()
