n = int(input())
# N x N tamaño del tablero
# F fichas
f = 0
ficha = False

for i in range(n):

    fila = input().strip()

    for j in range(n):

        # controlo no exceder el limite, si puedo poner ficha y no puse una ficha anteriormente
        if ((j+2) <= n) and (fila[j:j+2] == "NN") and (not ficha):
            f += 1
            ficha = True
        else:
            ficha = False # porque no puse ficha

print(f)