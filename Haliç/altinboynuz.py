# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 12:46:02 2021

@author: PC
"""

import cv2
import numpy as np

image=cv2.imread("kedi.jpg")
image[:,:,0]=50 #1. : işareti yükseklik 2. İşaret Genişlik 3. Alana rgb renk kodunu veriyoruz.
image[:,:,0]=200
cv2.imshow("Kedi",image)
cv2.waitKey(0)
cv2.destroyAllWindows()