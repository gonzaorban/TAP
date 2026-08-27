a, b, c = map(int, input().split()) # map aplica int a cada string y el desempaquetado asigna cada valor a una variable. Falla si no hay exactamente 3 números (ValueError: not enough values to unpack). Bien si sabés que siempre son 3.

mayor = max(a, b, c)
menor = min(a, b, c)
medio = a + b + c - mayor - menor # calculo el del medio

if mayor >= (medio + menor):
    print("S")
else:
    print("N")