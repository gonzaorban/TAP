#PROBLEMA J - Never Add Up to X
#funciona cuando ejecutamos con los 3 ejemplos pero en la pagina tira error

n, x = map(int,input().split())

belleza = list(map(int,input().split()))
belleza.sort() #puede o no estar

while True:

    contX = 0
    contM = 0
    for i in range(n):
        if (i+1 < n) and ((belleza[i] + belleza[i+1]) == x):
            contX += 1
            if (i + 2) <= (n - 1) and (belleza[i] != belleza[i+2]): #control indice
                resg = belleza[i+2]
                belleza[i+2] = belleza[i]
                belleza[i] = resg
                contM += 1
            elif (i - 2) >= 0 and (belleza[i] != belleza[i-2]):
                resg = belleza[i-2]
                belleza[i-2] = belleza[i]
                belleza[i] = resg
                contM += 1

        elif (i-1 > 0) and ((belleza[i] + belleza[i-1]) == x):
            contX += 1
            if (i + 2) <= (n - 1) and (belleza[i] != belleza[i+2]): #control indice
                resg = belleza[i+2]
                belleza[i+2] = belleza[i]
                belleza[i] = resg
                contM += 1
            elif (i - 2) >= 0 and (belleza[i] != belleza[i-2]):
                resg = belleza[i-2]
                belleza[i-2] = belleza[i]
                belleza[i] = resg
                contM += 1
        
    if contX == 0:
        print(belleza)
        break
    elif contM == 0:
        print("*")
        break
