# Lo termino haciendo Claude, me daba demasiado Time limit exceeded on test 28

import sys
from bisect import bisect_left

# Leo toda la entrada de una y la parto por espacios/saltos de linea.
# Con hasta 10^5 numeros por linea input() es lento, y ademas asi no dependo de que cada lista venga en una unica linea.
datos = sys.stdin.buffer.read().split()

n = int(datos[0]) # N cantidad de viajes
m = int(datos[1]) # M cantidad de oficinas

v = [int(x) for x in datos[2 : 2 + n]] # viajes

o = [int(x) for x in datos[2 + n : 2 + n + m]] # oficinas

salida = []

f = [] # filtro los empleados
minimo = float('inf') 
for e in o: 
    if e < minimo:
        f.append(e)
        minimo = e

total = len(f) # cantidad de oficinas que sobrevivieron al filtro

# f esta ordenado descendente, pero bisect solo trabaja sobre listas ascendentes. 
# Negando cada valor obtengo una lista ascendente con los MISMOS indices, asi que el indice que devuelve bisect sirve tal cual.
# La condicion f[j] <= r equivale a g[j] >= -r, y "primera posicion con valor >= x" es exactamente bisect_left.
g = [-e for e in f]

# Cada reparto efectivo corta el resto al menos por la mitad (si r >= e, entonces r % e < r/2),
# asi que con A <= 10^9 hay a lo sumo ~30 repartos reales por viaje.
#
# Hay dos escenarios opuestos y conviene una estrategia distinta en cada uno:
#
#   - f corto  (pocas oficinas sobrevivieron al filtro): las cadenas de
#     repartos son largas, pero recorrer f entero cuesta muy poco. Un
#     barrido lineal directo gana, porque evita el overhead de llamar a
#     bisect una vez por reparto.
#
#   - f largo  (muchas oficinas sobrevivieron): recorrerlo entero es
#     inviable, pero las cadenas resultan de apenas 1 o 2 repartos, asi
#     que las pocas busquedas binarias salen baratas.
#
# El umbral separa ambos regimenes.
UMBRAL = 64

if total <= UMBRAL:
    # Pocas oficinas: barrido lineal, sin busqueda binaria.
    for a in v: # alfajores
        r = a # resto de alfajores para Seba
        for e in f:
            if e <= r: # si alcanza para darle uno a cada empleado
                r %= e # reparte y se queda con el sobrante
        salida.append(r)
else:
    # Muchas oficinas: saltea las inutiles con busqueda binaria.
    for a in v: # alfajores

        r = a # resto de alfajores para Seba
        desde = 0 # primera oficina todavia sin visitar

        while desde < total:

            # Proxima oficina donde Seba puede repartir algo: la primera
            # posicion >= desde con f[j] <= r, buscada sobre los negados.
            j = bisect_left(g, -r, desde)

            if j == total:
                break # ninguna oficina restante puede repartir

            r = r % f[j] # reparte y se queda con el sobrante
            desde = j + 1 # sigue desde la oficina siguiente

        salida.append(r)

sys.stdout.write(' '.join(map(str, salida)))