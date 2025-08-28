# algo asi lo pensamos en la competencia 
n = int(input().strip())

xs = []
ys = []

for _ in range(n):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

xmin = min(xs)
xmax = max(xs)
ymin = min(ys)
ymax = max(ys)

# sumar 2 por el margen de 1 en cada lado
ancho = (xmax - xmin + 2)
alto = (ymax - ymin + 2)

perimetro = 2 * (ancho + alto)
print(perimetro)
