#memorama Fernando Morán A01284623
import random
def crear(num):
    lista_inicial = []
    for i in range(num):
        lista_inicial.append(i+1)
        lista_inicial.append(i+1)
    print(lista_inicial )
    random.shuffle(lista_inicial)
    print(lista_inicial )
    return lista_inicial
def crea_tablero(lista):
    matriz_inicial = []
    cont = 0
    sub_lista =[]
    for i in range(len(lista)):
        if (cont== 5):
            sub_lista.append(lista[i])
            matriz_inicial.append(sub_lista)
            sub_lista =[]
            cont = 0
        else:
            sub_lista.append(lista[i])
            cont = cont +1
    return matriz_inicial
def imprime_tablero(matriz):
    print("    {:^4} {:^4} {:^4} {:^4} {:^4} {:^4}".format(0,1,2,3,4,5))
    print('  |______________________________\n')  
    for i in range(len(matriz)):
        print(i, "|", end=' ' )
        for j in range(len(matriz[i])):
            print("{0:^4}".format(matriz[i][j]), end=' ')
        print('    \n')
def asteriscos(n):
    matriz=[]
    for  i in range (0,n):
        matrizsub=[]
        for  i in range (0,n):
            matrizsub.append("*")
        matriz.append(matrizsub)
    return (matriz)

def leer ():
    while True:
        num=input()
        if num.isdecimal() and num in ('0','1','2','3','4','5'):
            num=int(num)
            break
        else:
            print('da numero entre 0 y 5')
    return num
def main():
    print("***** bienvenido al memorama!! *****\n\n")

    lista = crear(18)
    tablero = crea_tablero(lista)
    tableroasteriscos=asteriscos(6)
    imprime_tablero(tablero)
    print("\n\n\nrespuestas arriba")
    imprime_tablero(tableroasteriscos)
    """linea 57 muestra respuestas"""
    turnojugador=1
    p1=0
    p2=0
    cambiarturno=0
    nom1=input(' player 1: ')
    nom2=input('player 2: ')  
    nohaycartas=0
    while True:
        print('Toca turno a player  ',turnojugador)
        while True:
            print('da renglon de 1er carta')
            carta1R= leer()
            print('da columna de 1er carta')
            carta1C=leer()
            print('da renglon de 2a carta')
            carta2R=leer()
            print('da columna de 2a carta')
            carta2C=leer()
            print( "posición carta 1 (",carta1R,carta1C ,") ,posición carta 2 (" ,carta2R,carta2C,")")
            print("numeros en cartas:",tablero[carta1R][carta1C], tablero[carta2R][carta2C])
            if tablero[carta1R][carta1C] == '*'  or tablero[carta2R][carta2C]=='*':
                print('carta abierta')
                continue
            if carta1R==carta2R and carta1C==carta2C:
                print('seleccionar cartas diferentes' )
                continue
            else:
                break
        if tablero[carta1R][carta1C]==tablero[carta2R][carta2C]:
            tableroasteriscos[carta1R][carta1C]=tablero[carta1R][carta1C]
            tableroasteriscos[carta2R][carta2C]=tablero[carta2R][carta2C]
            tablero[carta1R][carta1C]='*'
            tablero[carta2R][carta2C]='*'
            imprime_tablero(tablero)
            print("\n\n\n faltantes arriba")
            imprime_tablero(tableroasteriscos)
            cambiarturno=0
            print("punto para el jugador",turnojugador)
            if turnojugador==1:
                p1=p1+1
                print("puntos de",nom1,": " ,p1)
            else:
                p2=p2+1
                print(p2)
                print("puntos de",nom2,": " ,p2)
        else:
            cambiarturno=1
        if p1+p2>=18:
            print('ya no hay cartas')
            nohaycartas=1
        if nohaycartas==1:
                break
        while True:

            seguirjugando=input("Deseas seguir jugando s/n ")
            if seguirjugando in ('s','S','n','N'):
                if turnojugador==1 and cambiarturno==1:
                    turnojugador=2
                    break
                elif turnojugador==2 and cambiarturno==1:
                    turnojugador=1
                    break
                else:
                    break
        if seguirjugando == "n" or seguirjugando=="N":
            break
    if p1>p2:
        print("gano ",nom1)

    elif p2>p1:
        print("gano",nom2)
    else:
        print("empate!")
    print("puntos de",nom1,": " ,p1)
    print("puntos de",nom2,": " ,p2)
main()