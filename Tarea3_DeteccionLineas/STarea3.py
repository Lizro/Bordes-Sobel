def Orientacion(ang,pixeles):
    import math
    DAngulos=dict()
    theta=[]
    for i in pixeles:
        theta= int(90+ang[i])
        theta.append(theta)
        if theta==360:
            theta=0
        if theta not in DAngulo:
            DAngulos[theta]=1
        else:
            DAngulos[theta]+=1
    v=list(DAngulos.values())
    k=list(DAngulos.keys())
    a=v.index(max(v))
    return k[a]

def Regresor(fila,columna,CentroYB,CentroXB,Orientacion):
    import math
    x=1
    y=1
    x2=0
    y2=0
    radio=0
    radio2=0
    puntos=[]
    while(y<fila-1 and y>=1 and x<columna-1 and x>=1):
                x=int(round(CentroXB-radio*math.cos(math.radians(Orientacion))))
                y=int(round(CentroYB+radio*math.sin(math.radians(Orientacion))))
                x2=int(round(CentroXB-radio2*math.cos(math.radians(Orientacion))))
                y2=int(round(CentroYB+radio2*math.sin(math.radians(Orientacion))))
                if x<columna-1 and y<fila-1:
                    puntos.append((y,x))
                    puntos.append((y2,x2))
                radio-=1
                radio2+=1
            
    return puntos


def CajaEnvolvente2(pixeles):
    import math
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
    CentroXB= mcolumna+int((Mcolumna-mcolumna)/2)
    CentroYB= mfila+int((Mfila-mfila)/2)
    magnitud= math.sqrt((Mcolumna-mcolumna)**2 + (Mfila-mfila)**2)
    return CajaEnvolvente,CentroXB,CentroYB, magnitud
