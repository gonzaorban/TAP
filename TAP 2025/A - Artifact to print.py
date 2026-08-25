# A. Artifact to print

lista = input().strip()   # la línea con las 10 letras

tap = "TAP"
j = 0  # índice para la palabra "TAP"

for c in lista:
    if c == tap[j]:
        j += 1
        if j == 3:  # encontramos T, A y P en orden
            break

if j == 3:
    print("S")
else:
    print("N")
