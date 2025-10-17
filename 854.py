troom,tcond = map(int, input().split())
mode = input()
if mode == "freeze":
    if troom > tcond:
        print(tcond)
    else:
        print(troom)
elif mode == "heat":
    if troom < tcond:
        print(tcond)
    else:
        print(troom)
elif mode == "auto":
    print(tcond)
else:
    print(troom)
