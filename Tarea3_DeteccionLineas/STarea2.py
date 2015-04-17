#Se genera un color de manera aleatoria
import random
def color(a):
    R= int(random.random()*a)
    G= int(random.random()*a)
    B= int(random.random()*a)
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
    CentroXB=mcolumna+int((Mcolumna-mcolumna)/2)
    CentroYB=mfila+int((Mfila-mfila)/2)
    return CajaEnvolvente,CentroXB,CentroYB


def CentroMasa(pixeles):
    CentroY=[]
    CentroX=[]
    for i in pixeles:
        CentroY.append(i[0])
        CentroX.append(i[1])
    CentroY= sum(CentroY)/len(pixeles)
    CentroX= sum(CentroX)/len(pixeles)
    return CentroY,CentroX



                                         
                                
