n, q = map(int, input().split())
# N largo de la lista
# Q cantidad de partidas que se juegan
# L limite inferior sublista
# R limite superior sublista

lista = list(map(int, input().split()))

# Arrancan en n+1 posiciones porque la posicion 0 representa "cero elementos".
pot2 = [0] * (n + 1)   # suma de las potencias de 2 >= 2 (solo Agustin)
imp = [0] * (n + 1)    # suma de los impares >= 3 (solo Brian)
unos = [0] * (n + 1)   # cantidad de 1 (los pueden tomar los dos)

# Sumas acumuladas: la posicion i guarda el total de los primeros i elementos.
for i in range(n):
    x = lista[i]

    # cada posicion arranca copiando lo que venia acumulado
    pot2[i+1] = pot2[i]
    imp[i+1] = imp[i]
    unos[i+1] = unos[i]

    if x == 1:
        unos[i+1] += 1
    elif (x & (x - 1)) == 0: # Compara dos números bit por bit: pone 1 donde ambos tienen 1, y 0 en cualquier otro caso.
        pot2[i+1] += x
    elif x % 2 == 1:
        imp[i+1] += x
    # si no entra en ningun caso no lo puede tomar nadie, no suma

for i in range(q):

    l, r = map(int, input().split())

    # la suma de la sublista sale de restar los acumulados:
    # todo hasta r, menos todo lo que hay antes de l
    u = unos[r] - unos[l-1]
    a = pot2[r] - pot2[l-1]   # agustin
    b = imp[r] - imp[l-1]     # brian

    # los 1 se los reparten alternados, empezando por Agustin
    if (u % 2) == 0:
        a += (u // 2)
        b += (u // 2)
    else:
        a += ((u // 2) + 1)
        b += (u // 2)

    if a > b:
        print("A")
    elif a < b:
        print("B")
    else:
        print("E")
