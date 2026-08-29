n = int(input())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

s = 0
x = 0

pasar = 0

while pasar < 2:

    if pasar < 2 and x < n and max(a[x:n]) >= s:
        s = max(a[x:n])
        for i in range(len(a)):
            if a[i] == s:
                indice = i
        x = indice + 1 # indice del max
        pasar = 0
    else:
        pasar += 1

    if pasar < 2 and x < n and min(b[x:n]) <= s:
        s = min(b[x:n])
        for i in range(len(b)):
            if b[i] == s:
                indice = i
        x = indice + 1 # indice del max
        pasar = 0
    else:
        pasar += 1

print(s)
