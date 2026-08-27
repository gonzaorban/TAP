golesA1, golesP1 = map(int, input().split())

golesA2, golesP2 = map(int, input().split())

if (golesA1 + golesA2) > (golesP1 + golesP2):
    print("A")
elif (golesA1 + golesA2) < (golesP1 + golesP2):
    print("P")
else:
    print("D")