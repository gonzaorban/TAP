# Leer los tres valores: precio del alfajor (A), billete de Darío (B), y precio del caramelo (C)
A, B, C = map(int, input().split())

# Verificar si ese vuelto se puede dar con caramelos de valor C
# Es decir, si el vuelto es un múltiplo exacto de C
if ((B - A) % C) == 0:
    print("S")   # Sí se puede
else:
    print("N")   # No se puede
