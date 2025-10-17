k = int(input())
A = ["G", "C", "V"]
for i in range(k):
    A[1], A[2] = A[2], A[1]
    A[0], A[1] = A[1], A[0]
print("".join(A))
