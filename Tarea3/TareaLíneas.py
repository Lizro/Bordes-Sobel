#img imagen original
#ima2 bordes
#gx y gy gradientes en eje x y eje y
def lineas(img, ima2, gx, gy):
    f, c = ima2.shape
    frequency = dict()
    lines = dict()
    muestreo=30 #Valor de muestreo#
    rho1=dict() 
    for f1 in xrange(0,f,1):
        for c1 in xrange(0,c,1):
            if ima2[f1,c1]!=0:
                #Se redondea el ángulo para garantizar la detección de lineas horizontales#
                #y verticales#
                if gx[f1,c1] > 0 and gy[f1,c1] == 0:
                    theta = 0
                elif gx[f1,c1] < 0 and gy[f1,c1] == 0:
                    theta = 180
                if gx[f1,c1] == 0 and gy[f1,c1] > 0:
                    theta = 90
                elif gx[f1,c1] == 0 and gy[f1,c1] < 0:
                    theta = 270
                else:
                    theta = (int(math.degrees(math.atan2(gy[f1,c1],gx[f1,c1])))/muestreo)*muestreo

                rho = (int((c1*math.cos(theta)) + (f1*math.sin(theta)))/muestreo)*muestreo
                lines[f1,c1] = (theta, rho)
                if not (theta, rho) in frequency:
                    frequency[(theta, rho)] = 1
                    rho1[rho]=1
                else:
                    frequency[(theta, rho)] += 1
                    rho1[rho]+=1
            else:
                lines[f1, c1] = None

    #Se detectan y se marcan con un color diferente las líneas según la orientación#       
    for f1 in xrange(0,f,1):
        for c1 in xrange(0,c,1):
            if lines[f1,c1] in frequency:
                if lines[f1, c1][0] == 0 or lines[f1, c1][0] == 180:
                    img[f1,c1] = (0, 255, 0)
                elif lines[f1, c1][0] == 90 or lines[f1, c1][0] == 270:
                    img[f1,c1] = (0, 0, 255)
                else:
                    img[f1,c1] = (255, 0, 0) 

    fr=list(rho1.values())
    rhol=list(rho1.keys())

    #Se generan los datos necesarios para generar un histograma de los valores de ro en el programa R#
    b=open('histo.csv','w')
    for i in xrange(0,len(fr),1):
        print >> b,fr[i],',',rhol[i]
    b.close()
            
    cv2.imshow('Detección de Líneas',img)
    cv2.waitKey(0) & 0xFF
    cv2.destroyAllWindows()
    return img
