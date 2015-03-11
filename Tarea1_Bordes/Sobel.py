from Ejemplo import *
from edge import *
import cv2
import numpy as np
img2=rgb2gray('helados-3.jpg')
m=grad(img2)
umb=int(raw_input("El umbral es:  "))
f, c = m.shape
for f1 in xrange(0,f,1):
    for c1 in xrange(0,c,1):
        if m[f1,c1]<umb:
            img2[f1,c1]=0
        else:
            img2[f1,c1]=255
cv2.imshow('Imagen',img2)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
