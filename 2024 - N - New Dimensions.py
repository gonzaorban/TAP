n = int(input())
lista = list(map(int, input().split()))

# Caso 1: Si solo hay un valor, no se puede formar caja distinta
# Caso 2: usar 3 veces el mismo valor (ganancia = 0 siempre)

a, b, c = max(lista), max(lista), min(lista)

ganancia = a*a + b*b + c*c- (a*b + b*c + c*a)

print(ganancia)
