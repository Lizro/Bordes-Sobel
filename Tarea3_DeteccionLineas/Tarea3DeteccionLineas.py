from STarea2 import *   
from STarea3 import *   
import math

def DeteccionDeLineas(iBinaria2, ang):
    Salida=cv2.imread('Imagen.png',1)
    fila, columna = iBinaria2.shape
    fila1=0
    columna1=0
    Objetos=0
    Dcolores=dict()
    Angulos=[]
    Colores=[]

    while (fila1<fila):
        while (columna1<columna):
            if iBinaria2[fila1,columna1] == 255:
                pixeles, n=DFS(iBinaria2,fila1,columna1)
                EnvolventeB,CentroXB,CentroYB, magnitud = CajaEnvolvente2(pixeles)
                theta = Orientacion(ang,pixeles)
                puntos = Regresor(fila,columna,CentroYB,CentroXB,theta)
                R, G, B= color(255)
                if theta not in Angulos:
                    Angulos.append(theta)
                    Colores.append([R,G,B])
            
                Colorear= Colores[Angulos.index(theta)]

                for i in pixeles:
                    Salida[i]= Colorear
            
                for i in puntos:
                    Salida[i]=[0,0,255]
                    
                for a in [-2,-1,0,1,2]:
                        for b in [-2,-1,0,1,2]:
                             Salida[(CentroYB+a,CentroXB+b)]=[100,0,255]
                         
                if theta !=0 and theta !=180 and theta !=90 and theta !=270:
                    m= -1*float(math.cos(theta))/float(math.sin(theta))
                    b= magnitud/float(math.sin(theta))
                    cv2.putText(out,"y=%.2fx+%.2f" %(m,abs(b)), (CentroXB+8,CentroYB-8), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255,0,0))

                Objetos+=1
            columna1=columna1+1
        columna1=0
        fila1=fila1+1

    return Salida


