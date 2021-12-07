# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 11:30:51 2021

@author: PC
"""
import cv2 #OpenCV projeye import (yükeleme yapıyoruz)
import numpy as np #Görüntü işlemede matematiksel işlemler dolaylı yoldan geldiği için numpy kütüphanesini improt ettik.

image=cv2.imread("logo.png") #Dosya dizininden resimimizi image değişkenine aktardık.
cv2.imshow("MySql",image) # Dizinden çektiğimiz logo.png resimine manipülasyon uygulamak için yeniden adlandırdık.
print(image) #Image değişkenini yazdırıyoruz.
cv2.waitKey(0) #Penccere açık kalması için yazıyoruz.
cv2.destroyAllWindows() # Windows platformunda çalıştığımız için windows açılır penceresini kullanıyoruz.