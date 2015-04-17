#The predominant angle is detected
def Orientacion(ang,visitados):
    import math
    gn=dict()
    th=[]
    for i in visitados:
        theta=int(90+ang[i])
        th.append(theta)
        if theta==360:
            theta=0
        if theta not in gn:
            gn[theta]=1
        else:
            gn[theta]+=1
    v=list(gn.values())
    k=list(gn.keys())
    a=v.index(max(v))
    return k[a]

#from the Hough transform, the linear regressor is calculated
#for each line detected
def Regresor(h,w,By,Bx,angulo):
    import math
    x=1
    y=1
    x2=0
    y2=0
    r=0
    r2=0
    pt=[]
    while(y<h-1 and y>=1 and x<w-1 and x>=1):
                x=int(round(Bx-r*math.cos(math.radians(angulo))))
                y=int(round(By+r*math.sin(math.radians(angulo))))
                x2=int(round(Bx-r2*math.cos(math.radians(angulo))))
                y2=int(round(By+r2*math.sin(math.radians(angulo))))
                if x<w-1 and y<h-1:
                    pt.append((y,x))
                    pt.append((y2,x2))
                r-=1
                r2+=1
            
    return pt

#The bounding box and additional parameters are calculated
def CajaEnvolvente2(visitados):
    import math
    h=[]
    w=[]
    box=[]
    for i in visitados:
        h.append(i[0])
        w.append(i[1])
    Mh=max(h)
    mh=min(h)
    Mw=max(w)
    mw=min(w)
    for i in range(mw, Mw):
        box.append((mh,i))
    for i in range(mh,Mh+1):
        box.append((i,Mw))
    for i in range(mh+1,Mh):
        box.append((i,mw))
    for i in range(mw,Mw):
        box.append((Mh,i))
    Bmx=mw+int((Mw-mw)/2)
    Bmy=mh+int((Mh-mh)/2)
    mag=math.sqrt((Mw-mw)**2 + (Mh-mh)**2)
    return box,Bmx,Bmy, mag
