lista = input()

puntuacion = 0

for i in range(len(lista)):
    if lista[i:i+2] == "ha":
        puntuacion += 1
    elif lista[i:i+5] == "boooo":
        puntuacion -= 1
    elif lista[i:i+5] == "bravo":
        puntuacion += 3

print(puntuacion)