precio=0
precioTot=0
precioTotal=0
ventas=[]

def total_antes_descuento(x,y):
    z=x*y
    return(z)
def calcula_descuento(x,y):
    z=x*y
    return(z)
while True:
    while True:
        compra=[]
        nom=input('nombre')
        compra.append(nom)
        tipo=input('que tipo de silla quiere?(B/E/L)')
        if tipo==("B"):
            precio=700
            break
        elif tipo==("E"):
            precio=900
            break
        elif tipo==("L"):
            precio=1500
            break
        else:
            print("da valor correcto")
    while True:
        cliente=input('que tipo de cliente es?(F/N)')
        if cliente==("F"):
            desc=.80
            break
        elif cliente==("N"):
            desc=1
            break 
        else:
            print("da letra indicada") 
    while True:
        numero=int(input('cuantas sillas quieres?'))
        if numero>0:
            compra.append(numero*desc*precio)
            ventas.append(compra)
            break
        else:
            print("da numero válido")
    while True:
        seguir=input('quieres seguir comprando sillas? (S/N)')
        if seguir in ('S','N'):
            break        
    
    if seguir==("N"):
            precioTot=total_antes_descuento(numero,precio)
            print("precio sin descuento es: ",precioTot)
            if desc==1:
                resultado=calcula_descuento(desc,precioTot)
                if resultado>=20000:
                    print("descuento: ",(resultado*0.15))
                    print("precio con descuento es:",(resultado*0.85))
                elif 20000>resultado>=10000:
                    print("descuento: ",(resultado*0.1))
                    print("precio con descuento es:", (resultado*0.9))
                else:
                    print("no hay descuento")
                    print("precio es", resultado)
            else:
                resultado=calcula_descuento(desc,precioTot)
                print("descuento: ",(resultado*0.2))
                print("precio con descuento es: ",calcula_descuento(desc,precioTot)) 
            precioTotal=total_antes_descuento(numero,precio)+precioTotal
            break
    else:
        precioTot=total_antes_descuento(numero,precio)
        print("precio sin descuento es: ",precioTot)
    if desc==1:
        resultado=calcula_descuento(desc,precioTot)
        if resultado>=20000:
            print("descuento: ",(resultado*0.15))
            print("precio con descuento es:",(resultado*0.85))
        elif 20000>resultado>=10000:
            print("descuento: ",(resultado*0.1))
            print("precio con descuento es:", (resultado*0.9))
        else:
            print("no hay descuento")
            print("precio es", resultado)
    else:
        resultado=calcula_descuento(desc,precioTot)
        print("descuento: ",(resultado*0.2))
        print("precio con descuento es: ",calcula_descuento(desc,precioTot)) 
        precioTotal=total_antes_descuento(numero,precio)+precioTotal
    


    
print("precio total todos sin descuento es: ",precioTotal)
print(ventas)
f=open("ventas.txt","a")
for i in  range(len(ventas)):
    for j in range(len(ventas[i])):
        print(ventas[i][j])
        f.write(str(ventas[i][j])+ " ")
f.close()

        
        