h, m, s = map(int, input().split())

if h == 2:
    if m == 30:
        if s == 0:
            print("=")
        else:
            print("+")
    elif m > 30:
        print("+")
    else:
        print("-")
elif h >= 3:
    print("+")
else:
    print("-")
