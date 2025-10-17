n=input()
d=[int(i) for i in n]
if sum(d[:3]) == sum(d[3:]):
    print("YES")
else:
    print("NO")