n, k = map(int, input().split())
# N reyes
# K movimientos
# eje X
# eje Y

import math

# iniciales nomas
r, c = map(int, input().split())
maxX = r
minX = c
maxY = r
minY = c

# obtengo los reyes
for _ in range(n):
    x, y = map(int, input().split())
    reyes.append((x, y))

    maxX = max(maxX, x)
    minX = min(minX, x)
    maxY = max(maxY, y)
    minY = min(minY, y)

a = (maxX - minX) * (maxY - minY) # calcular el area

# calculo las esquinas
esq1X = minX
esq1Y = maxY
esq2X = maxX
esq2Y = maxY
esq3X = maxX
esq3Y = minY
esq4X = minX
esq4Y = minY

salidas = []

for puntos in reyes:
    
    d1 = math.isqrt((esq1X-puntos[0])**2+((esq1Y-puntos[1])**2))
    d2 = math.isqrt((esq2X-puntos[0])**2+((esq2Y-puntos[1])**2))
    d3 = math.isqrt((esq3X-puntos[0])**2+((esq3Y-puntos[1])**2))
    d4 = math.isqrt((esq4X-puntos[0])**2+((esq4Y-puntos[1])**2))

    d= min(d1, d2, d3, d4)

    if d >= k: # no puedo llegar a una esquina
        salidas.append(a)
    else: 
        k1 = d - 

a += x * k + y + k # sumo el lado X + celda de la esquina

a += x + y * k + k # sumo el lado X + celda de la esquina

# estas parado en una esquina
a += x * k + y * k + k ** 2 # sumo los dos lados + celda de la esquina