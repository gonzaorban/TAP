import math

n = int(input())
# N lanzamientos

w, l, tx, ty = map(int, input().split())
# dimesion de la cancha
# coordenadas del tejin

distanciasA = []
distanciasR = []

# totalizadores
a = 0
r = 0

for i in range(n):
    x, y = map(int, input().split())
    d = math.sqrt((tx-x)**2+((ty-y)**2))
    distanciasA.append(d)
ordA = sorted(distanciasA)

for i in range(n):
    x, y = map(int, input().split())
    d = math.sqrt((tx-x)**2+((ty-y)**2))
    distanciasR.append(d)
ordR = sorted(distanciasR)

if ordA[0] < ordR[0]:
    a += 1
    for c in ordA[1:]:
        if c < ordR[0]: # hasta que encuentre algun tejo mas cercano
            a += 1
        else:
            break
    print("A"," ",a)
else:
    r += 1
    for c in ordR[1:]:
        if c < ordA[0]:
            r += 1
        else:
            break
    print("R"," ",r)