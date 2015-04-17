from STarea2 import *     
from STarea3 import *     
import math

def DeteccionCirculos(iBinaria2, ang):
    salida=cv2.imread('Imagen.png',1)
    fila, columna = iBinaria2.shape
    fila1=0
    columna1= 0
    Objetos=0

    while (fila1<fila):
        while (columna1<columna):
            if iBinaria2[fila1,columna1] == 255:
                votos=dict()
                pixeles=[]
                pixeles2=[]
                puntos=[]
                j=0
                pixeles, n=DFS(iBinaria2,fila1,columna1)
                EnvolventeB,CentroXB,CentroYB =CajaEnvolvente(pixeles)
                pixeles2, n= DFS(iBinaria2,CentroYB,CentroXB)
                pr=round(float(n)/float(columna*fila)*100,2)
                votos[(CentroYB,CentroXB)]=1
                R, G, B=color(255)
                angulos=dict()

                while j<len(pixeles):
                    i=pixeles[j]
                    theta=int(ang[i])
            
                    puntos = Regresor(fila,columna,i[0],i[1],theta)
                    for i in puntos:
                       if i not in votos:
                            votos[i]=1
                        else:
                            votos[i]+=1
                    j+=1
                
                valores=list(votos.values())
                claves=list(votos.keys())
                a=valores.index(max(valores))
                center=claves[a]
                
                for i in pixeles2:
                    salida[i]=[R,G,B]

                for a in range(-4,5):
                    for b in range(-4,5):
                            salida[(center[0]+a,center[1]+b)]=[0,0,255]
                         
                radio=int(round(math.sqrt(n/float(3.1416))))
                A=-2*center[1]
                B=-2*center[0]
                C=int((center[0])**2 +(center[1])**2-(radio)**2)
                Objetos+=1
                for theta in xrange(0,360):
                    y=int(round(center[0]+radio*math.sin(math.radians(theta))))
                    x=int(round(center[1]-radio*math.cos(math.radians(theta))))
                    salida[y,x]=[0,0,255]
                    cv2.putText(salida,"C %d: X^2+Y^2+ %dX+%dY+%d" %(Objetos,A,B,C), (center[1]-10,center[0]-6), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.6, (255,0,0))
                           
            columna1=columna1+1
        columna1=0
        fila1=fila1+1

    return salida 


