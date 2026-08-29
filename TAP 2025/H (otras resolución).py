import math

n = int(input())

divisores = list(map(int, input().split()))

if (n == 1):
    if (divisores[0] == 1):
        print("*")
    else:
        print(divisores[0], 1) # el numero es primo
else:
    divisores.sort()
    divisoresSet = set(divisores) 
    
    MisteriosoEnLista = True
    
    for c in divisores:
        if ((divisores[-1] % c) != 0):
            MisteriosoEnLista = False

    
    if MisteriosoEnLista:
        # busco el divisor
        todosDivisibles = True
        for c in divisores:
            if (divisores[-1] // c) not in divisoresSet:
                divisorFaltante = divisores[-1] // c
                todosDivisibles = False
                break

        if todosDivisibles and (((math.sqrt(divisores[-1])) % 1) == 0) and ((math.isqrt(divisores[-1])) not in divisoresSet):
            print(divisores[-1], math.isqrt(divisores[-1]))  
        elif todosDivisibles:
           mayor = (divisores[1]) * (divisores[-1])
           print(mayor, mayor)
        else:
           print(divisores[-1], divisorFaltante)  
    else:
        mayor = (divisores[1]) * (divisores[-1])
        print(mayor, mayor)