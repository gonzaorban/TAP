# Solución al problema "G. Garlands"

# Leer el string de entrada
lista = input().strip()

# Contar cada letra necesaria
count_T = lista.count('T')
count_P = lista.count('P')
count_A = lista.count('A')
count_U = lista.count('U')

# En cada guirnalda necesitamos:
# - una T
# - una P
# - y una letra que sea A o U
count_AU = count_A + count_U

# El máximo número de guirnaldas posibles es el mínimo de esos tres
result = min(count_T, count_P, count_AU)

print(result)
