#Se calcula un histograma de las magnitudes en los gradientes en cada pixel obtenidos a través del Método Sobel.

data1<-read.csv("test.csv",header=FALSE,sep=",")
F<-data1[1] # Frecuencias absolutas
G<-data1[2] # magnitudes de gradientes
dat<-c()
e=1
for (i in 1:dim(G)[1]) {
 for (j in 1:F[i,1]){
  dat[e]=G[i,1]
  e=e+1 
  }}


hist(dat,breaks=20)

print('Listo')
