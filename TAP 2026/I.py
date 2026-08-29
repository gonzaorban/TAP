n, k = map(int, input().split())

if k == 1:
    print("S")
elif (k % 2) == 1 and n == 2: # impar
    print("S")
else:
    print("N")
