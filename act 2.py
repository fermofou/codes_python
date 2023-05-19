col=3
cal=[]
lalu=[]
promedio=[]
lista=[]
while True:
    nom=input('dame un nombre ')
    lalu.append(nom)
    renglon=[]
    p=0
    for k in range (col):
        while True:
            n=int(input('dame calificacion '))
            if 0<n<=10:
                break
            else:
                print('da valor de 0 a 10')
        renglon.append(n)
        p=p+n
    cal.append(renglon)
    p=p/3
    promedio.append(p)
    while True:
        x=input('Quieres agregar otro alumno? (s/n)')
        if x in ("s","n"):
            break
    if x=="n":
        break
for i in range(len(lalu)):
    lista.append(lalu[i])
    lista.append(cal[i])
print('Lista de alumnos con su calificación y promedio')
for i in range(0,len(lista),2):
    print('alumno ', lista[i],lista[i+1])
    
d=0
for i in range (len(promedio)):
    d=d+promedio[i] 
print ('el promedio del grupo es:',d/(len(promedio)))
print('La lista de alumnos es ',lista)
print ('La lista de promedio de alumnos es ',promedio)
nom=input('da nombre de archivo a crear: ')
f=open(nom+".txt","a")
f.write(str(lista))
f.close()
f=open(nom+".txt","r")
for x in f:
    print(x)
f.close()
