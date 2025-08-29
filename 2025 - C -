# (este es puro chat, no pude sacarlo)

# Leemos la entrada
n = int(input())
lista = list(map(int, input().split()))

# Convertimos a 0-based para simplificar
A = [x - 1 for x in lista]

# freq[v] contará cuántos índices i cumplen (A[i] + i) % n == v
freq = [0] * n

# Primer barrido: calculamos las clases (A[i] + i) % n
for i, a in enumerate(A):
    v = (a + i) % n
    freq[v] += 1

# Segundo barrido: para cada posición j, sumamos la frecuencia de su clase
total = 0
for j, a in enumerate(A):
    v = (a + j) % n
    total += freq[v]

# Mostramos la respuesta final
print(total)
