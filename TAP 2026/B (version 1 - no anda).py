lista = list(input())

gas = 0
vocales = ["A", "E", "I", "O", "U"]
setVocales = set(vocales)
i2 = 0

indice = len(lista)

for i in range(len(lista)):

    if (((i + 3) < indice) and (i > 0) and (lista[i] == "G")):
        if ((lista[i:(i+3)] == ["G","A","S"]) and (lista[i-1] == lista[i+3]) and ((lista[i-1]) in setVocales)):
            lista.pop(i-1) # borro vocal
            # borro GAS
            lista.pop(i-1)
            lista.pop(i-1)
            lista.pop(i-1)
            gas += 1

            # actualizo
            i2 = i # revisar
            indice = len(lista)
            break

for j in range(indice - i2):

    if ((((j+i2) + 3) < indice) and ((j+i2) > 0) and (lista[(j+i2)] == "G")):
        # rango | GAS | misma vocal | si son vocales
        if ((((j+i2)-1) >= i2) and (lista[(j+i2):((j+i2)+3)] == ["G","A","S"]) and (lista[(j+i2)-1] == lista[(j+i2)+3]) and ((lista[(j+i2)-1]) in setVocales)):
            gas += 1
            break

if gas == 1:
    print(''.join(map(str, lista)))
elif (gas >= 2):
    print("+")
else:
    print("-")
