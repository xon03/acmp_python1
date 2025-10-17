s,t = map(int, input().split())
if s<t:
    k=t-s
else:
    k=12+t-s
print(k)