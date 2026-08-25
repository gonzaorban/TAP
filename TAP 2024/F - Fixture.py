N = int(input()) # Numeros entre 1 y 100

results = [int(x) for x in input().split()]
total = 0
ganados = 0

for match in results:
    if match == 1:
        total += 1
        ganados += 1
        if ganados > 2:
            total += 1
    else:
        total -= 1
        ganados = 0

print(total)