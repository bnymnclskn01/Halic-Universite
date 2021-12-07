# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 13:05:27 2021

@author: PC
"""

import cv2
import numpy as np

image=cv2.imread("logo.png",0)
cv2.imshow("Twitter Logo",image)
print(image)
print(image.dtype)
print(image.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()