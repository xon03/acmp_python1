A1, A2, A3, B1, B2, B3 = map(int, input().split())
A=[A1, A2, A3]
B=[B1, B2, B3]
A.sort()
B.sort()
s=0
for i in range(3):
    s=s+A[i]*B[i]
print(s)