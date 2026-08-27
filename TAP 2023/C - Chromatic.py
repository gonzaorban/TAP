n = int(input())

r = sorted(map(int, input().split())) # ascendente
a = sorted(map(int, input().split()), reverse=True) # descendente

sumas = []

for i in range(n):
    sumas.append(r[i] + a[i])

print((max(sumas)-(min(sumas))))