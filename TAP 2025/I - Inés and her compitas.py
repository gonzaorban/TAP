n, m = map(int, input().split())

s = [0] * (n + 1) # +1 por ines

for _ in range(m):

    x, y = map(int, input().split())

    ronda = list(map(int, input().split()))

    b = ronda.count(1)

    if y > (x // (b+1)):
        s[n] += y
    else:
        b += 1
        s[n] += x // b

    for i in range(n):
        if ronda[i] == 1:
            s[i] += x // b
        else:
            s[i] += y

print(' '.join(map(str, s)))