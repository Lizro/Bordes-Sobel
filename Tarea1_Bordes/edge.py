#Variables: f=fila; c=columna
#Variables: Var1=Variable1; Var2=Variable2; Var3=Variable3; Var4=Variable4
#Se calculan las magnitudes de los gradientes a través de
#la máscara de detección de borde Sobel.
import cv2
import numpy as np
def grad(img2):
    f, c = img2.shape
    m=np.empty((f, c))
    frecuencias=dict()
    f1=0
    c1=0
    while (f1<f):
        while (c1<c):
            #Se establece una regla para eliminar posibles conflictos
            #causados por el efecto "dona".
            if c1==c-1:
                c2=c1
                var1=0
            else:
                c2=c1+1
                var1=1
            if f1==f-1:
                f2=f1
                var2=0
            else:
                f2=f1+1
                var2=1
            if c1>=c-2:
                c3=c1
                var3=0
            else:
                c3=c1+2
                var3=1
            if f1>=f-2:
                f3=f1
                var4=0
            else:
                f3=f1+2
                var4=1
            #Se aplica la máscara de detección de bordes Sobel sobre los ejes X y Y.
            con1x=-1*img2[f1, c1].tolist()+0*img2[f1, c2].tolist()*var1+1*img2[f1, c3].tolist()*var3
            con2x=-2*img2[f2, c1].tolist()*var2+0*img2[f2, c2].tolist()*var2*var1+2*img2[f2, c3].tolist()*var2*var3
            con3x=-1*img2[f3, c1].tolist()*var4+0*img2[f3, c2].tolist()*var4*var1+1*img2[f3, c3].tolist()*var4*var3
            convx=con1x+con2x+con3x

            con1y=1*img2[f1, c1].tolist()+2*img2[f1, c2].tolist()*var1+1*img2[f1, c3].tolist()*var3
            con2y=0*img2[f2, c1].tolist()*var2+0*img2[f2, c2].tolist()*var2*var1+0*img2[f2, c3].tolist()*var2*var3
            con3y=-1*img2[f3, c1].tolist()*var4-2*img2[f3, c2].tolist()*var4*var1-1*img2[f3, c3].tolist()*var4*var3
            convy=con1y+con2y+con3y
            #Se calcula la magnitud del gradiente
            g=max(abs(convx),abs(convy))
            m[f1,c1]=g
            gst=str(g)
            #Se genera un diccionario con las frecuencias absolutas y las magnitudes de los gradientes.
            if gst not in frecuencias:
                frecuencias[gst]=1
            else:
                frecuencias[gst]+=1
            c1=c1+1
        c1=0
        f1=f1+1
    #Se generan listas a partir de la información disponible en el diccionario.
    fr=list(frecuencias.values())
    gr=list(frecuencias.keys())  
    gr2=map(int, gr)
    #Se genera un archivo CVS para almacenar las frecuencias absolutas y las magnitudes del gradiente.
    b=open('test.csv','w')
    for i in xrange(0,len(fr),1):
        print >> b,fr[i],',',gr[i]
    b.close()
    #Como salida se obtiene una matriz con los valores de los gradientes.
    return m
