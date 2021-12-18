# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 01:21:51 2021

@author: PC
"""

import cv2
import numpy as np
resim=cv2.imread("ataturk.jpg")
aynalamaResim=cv2.copyMakeBorder(resim,75,75,125,125,cv2.BORDER_REFLECT)
uzatilanResim=cv2.copyMakeBorder(resim,120,120,120,120,cv2.BORDER_REPLICATE)
tekrarlananResim=cv2.copyMakeBorder(resim,120,120,120,120,cv2.BORDER_WRAP)
sarilanResim=cv2.copyMakeBorder(resim,50,50,50,50,cv2.BORDER_CONSTANT,
                                value=(75,150,255))
cv2.imshow("Atatürk",aynalamaResim)
cv2.imshow("Uzatılan Atatürk",uzatilanResim)
cv2.imshow("Tekrarlanan Atatürk",tekrarlananResim)
cv2.imshow("Sarılan Atatürk",sarilanResim)
cv2.waitKey(0)
cv2.destroyAllWindows()