N = int(input())
A = [int(input()) for i in range(N)]
m = A[0]+A[7]
for i in range(N-7):
    for j in range(7, N):
        if A[i] + A[j] > m:
            m = A[i] + A[j]
print(m)
