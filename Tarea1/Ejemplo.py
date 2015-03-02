#Tarea 1; Deteccion de Bordes
#Variables: f=fila; c=columna
#Variables: Var1=Variable1; Var2=Variable2; Var3=Variable3; Var4=Variable4
#Con el objetivo de reducir el coste computacional, se transforma una imagen en RGB
#a escala de grises.
import numpy as np
import cv2
def rgb2gray(img):
    img=cv2.imread(img,1)
    f, c, d = img.shape
    f1=0
    c1=0
    while (f1<f):
        while (c1<c):
            if c1==0:
                var2=0
            else:
                var2=1
            if c1==0:
                var1=0
            else:
                var1=1
            #Se establece una regla para eliminar posibles conflictos
            #causados por el efecto "dona".
            if c1==c-1:
                c2=c1
                var4=0
            else:
                c2=c1+1
                var4=1

            if f1==f-1:
                f2=f1
                var3=0
            else:
                f2=f1+1
                var3=1
            #Se requiere de una subrutina para realizar la suma de los vecinos del pixel actual
            #para cada canal RGB respectivamente.
            for i in range(len(img[f1, c1].tolist())):
                sum1=img[f1-1, c1-1].tolist()[i]*var1*var2+img[f1-1, c1].tolist()[i]*var1+img[f1-1, c2].tolist()[i]*var1*var4
                sum2=img[f1, c1-1].tolist()[i]*var2+img[f1, c1].tolist()[i]+img[f1, c2].tolist()[i]*var4
                sum3=img[f2, c1-1].tolist()[i]*var2*var3+img[f2, c1].tolist()[i]*var3+img[f2, c2].tolist()[i]*var3*var4
                #Se calcula la media.
                med=(sum1+sum3+sum3)//(var1*var2+var1+var1*var4+var2+var4+var2*var3+var3+var3*var4+1)
            #El valor de la media se asigna a cada canal RGB.
            img[f1, c1]=[med,med,med]
            #print (a*b+a+a*d+b+d+b*c+c+c*d)
            c1=c1+1
        c1=0
        f1=f1+1
    #Se tiene como salida una imagen en escala de grises de un solo canal denotado por img2.  
    img2=img[:,:,0]
    return img2


