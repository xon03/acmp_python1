a,b,c,t = map(int, input().split())
if a>=t:
    d=t*b
else:
    d=a*b+(t-a)*c
print(d)