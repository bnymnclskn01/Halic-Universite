# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 13:47:07 2021

@author: PC
"""

import cv2
import numpy as np

image=cv2.imread("kedi.jpg")
cv2.imshow("Yavru Aslan",image)
print("Resim Renk Kodları"+str(image[220,175]))
print("Resim Boyutu"+str(image.size))
print("Resim Özellikleri"+str(image.shape))
print("Resim Veri Tipi"+str(image.dtype))
cv2.waitKey(0)
cv2.destroyAllWindows()