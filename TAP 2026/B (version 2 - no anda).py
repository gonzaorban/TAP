lista = list(input())

gas = 0
vocales = ["A", "E", "I", "O", "U"]
setVocales = set(vocales)
i2 = 0

indice = len(lista)

salida = []
gas = 0
indice2 = 0
bandera = True

for i in range(len(lista)):
    palabra = lista[i]
    if palabra in setVocales:
        if ((i+4) <= indice):
            if lista[i+1] == "G":
                if lista[i+2] == "A":
                    if lista[i+3] == "S":
                        if lista[i+4] == palabra:
                            gas += 1
                            indice2 = i+4
                            bandera = False
                            break
    salida.append(palabra)

if not bandera:
    salida.append(lista[indice2])

if indice2 < indice:

    for i2 in range(len(lista[indice2:indice])):
        palabra = lista[indice2+i2]

        if palabra in setVocales:
            if ((i2+4) <= indice):
                if lista[i2+1] == "G":
                    if lista[i2+2] == "A":
                        if lista[i2+3] == "S":
                            if lista[i2+4] == palabra:
                                gas += 1
                                break
        salida.append(palabra)

if gas == 1:
    print(''.join(map(str, salida)))
elif (gas >= 2):
    print("+")
else:
    print("-")
