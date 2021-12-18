# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 01:37:37 2021

@author: PC
"""

import cv2
import numpy as np
resim=cv2.imread("resim.jpg")
cv2.rectangle(resim,(50,100),(150,30),[0,0,255],2)
cv2.imshow("Resim",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()