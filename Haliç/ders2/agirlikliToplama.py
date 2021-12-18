# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 01:31:06 2021

@author: PC
"""

import cv2
import numpy as np
resim1=cv2.imread("kirmizi.png")
resim2=cv2.imread("mavi.jpg")
print(resim1[250,270])
print(resim2[300,350])
cv2.imshow("Kırmızı",resim1)
cv2.imshow("Mavi",resim2)
print(resim1[250,270]+resim2[300,350])
cv2.waitKey(0)
cv2.destroyAllWindows