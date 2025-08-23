#PROBLEMA L - Games
#no anda pero la logica esta

n, q = map(int, input().split())

lista = list(map(int, input().split()))
potencias = []
impares = []

#calculos previos
for i in range(len(lista)):
    if ((lista[i] & (lista[i] - 1)) == 0) and (lista[i] > 1):
        potencias.append(lista[i])
    elif ((lista[i] % 2) == 1) and (lista[i] > 1):
        impares.append(lista[i])

#juego general
for i in range(0,q):
    l, r = map(int, input().split())
    jugando = lista[l-1:r]

    a = 0
    b = 0

    for i in jugando:
        if i in potencias:
            a += i
        if i in impares:
            b += i
        if i == 1:
            cant1 += 1

    mitadCant = cant1 // 2

    if (cant1 % 2) == 1:
        a += mitadCant + 1 #sumo +1 porque agustin juega primero
        b += mitadCant
    else:
        a += mitadCant
        b += mitadCant

    if a > b:
        print("A")
    elif a < b:
        print("B")
    else:
        print("E")
