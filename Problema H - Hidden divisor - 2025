n = int(input())
lista = list(map(int,input().split()))
lista.sort() # ordena la lista
import math # math es un módulo estándar de Python

divisor_set = set(lista) # solamente se usa para el acceso rapido
encontrado = False

if n == 1:
    if lista[0] == 1:
        print("*") # no se puede calcular (el numero puede ser cualquiera de los primos)
        encontrado = True
    else:
        # el caso de los numeros primos
        print(lista[0], 1) # num a encontrar, num faltante
        encontrado = True
else:
    ult = lista[len(lista) - 1]

    for c in lista:
        # si el num faltante es el mayor
        if ((ult % c) != 0):
            # ult * lista[1] es una operacion que es el primer divisor distinto de 1 y el ultimo divisor del numero, te da el numero a encontrar
            print(ult * lista[1], ult * lista[1])
            encontrado = True 
            break
        
        # si el num faltante no es el mayor, buscas el divisor que te falta
        elif ((ult // c) not in divisor_set):
            print(ult, ult // c)
            encontrado = True
            break
    
    # X es potencia de primos
    if (encontrado == False):
        # si el numero faltante es la raiz de X 
        if ((math.sqrt(ult) % 1) == 0) and ((math.isqrt(ult)) not in divisor_set):
            print(ult, math.isqrt(ult))
        else:
            # si el num faltante es el mayor
            print(ult * lista[1], ult * lista[1])
