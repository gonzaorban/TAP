n = int(input())

lista = list(map(int, input().split()))

pasaje = [0, 5, 1, 6, 2, 7, 3, 8, 4]

salida = [0] * n

for i in range(len(lista)):

    salida[i] = pasaje[lista[i]]

print(' '.join(map(str,salida)))
