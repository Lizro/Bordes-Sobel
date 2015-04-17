#Se genera un color de manera aleatoria
import random
def color(xo):
    R= int(random.random()*xo)
    G= int(random.random()*xo)
    B= int(random.random()*xo)
    return R,G,B

#Busqueda por profundidad
def DFS(Binaria,fila1,columna1):
    fila, columna= Binaria.shape
    marca= 254
    frecuencias= dict()
    CantPixeles= 0
    pixeles=[]
    Contenedor=[]
    Contenedor.append((fila1,columna1))
    original= Binaria[(fila1,columna1)]
    while len(Contenedor) > 0:
        (fila1, columna1)= Contenedor.pop(0)
        actual = Binaria[fila1, columna1]
        if actual == original or actual == marca:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    i, j = (fila1 + dx, columna1 + dy)
                    if i >= 0 and i < fila and j >= 0 and j < columna:
                        contenido = Binaria[i, j]
                        if contenido == original:
                            Binaria[i, j]= marca
                            pixeles.append((i,j))
                            CantPixeles += 1
                            Contenedor.append((i, j))
    return pixeles, CantPixeles

#Generar la caja envolvente
def CajaEnvolvente(pixeles):
    fila=[]
    columna=[]
    CajaEnvolvente=[]
    for i in pixeles:
        fila.append(i[0])
        columna.append(i[1])
    Mfila=max(fila)
    mfila=min(fila)
    Mcolumna=max(columna)
    mcolumna=min(columna)
    for i in range(mcolumna, Mcolumna):
        CajaEnvolvente.append((mfila,i))
    for i in range(mfila,Mfila+1):
        CajaEnvolvente.append((i,Mcolumna))
    for i in range(mfila+1,Mfila):
        CajaEnvolvente.append((i,mcolumna))
    for i in range(mcolumna,Mcolumna):
        CajaEnvolvente.append((Mfila,i))
    Bmx=mcolumna+int((Mcolumna-mcolumna)/2)
    Bmy=mfila+int((Mfila-mfila)/2)
    return CajaEnvolvente,Bmx,Bmy

#A correction of an strange object produced in the preprocessing
def corrige(bina,fila,w):
    c=0
    ch=1
    cw=1
    cfila=1
    while (c==0):
        if bina[0,w-cw]==255:
            cw+=1
        else:
            c=1
    c=0
    while (c==0):
        if bina[fila-ch,0]==255:
            ch+=1
        else:
            c=1
    return ch-1,cw-1

#Calculation of the center of mass
def centroide(visitados):
    Ch=[]
    Cw=[]
    for i in visitados:
        Ch.append(i[0])
        Cw.append(i[1])
    Ch=sum(Ch)/len(visitados)
    Cw=sum(Cw)/len(visitados)
    return Ch,Cw



                                         
                                
