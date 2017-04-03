N = int(input("Количество вершин:"))

G = [[int(x) for x in input().split()] for i in range(N)]
W = [G] + [[[None]*N for i in range(N)] for k in range(N)]
for k in range(0, N):
    for i in range(N):
        for j in range(N):
            W[k+1][i][j] = min(W[k][i][j], W[k][i][k] + W[k][k][j])
A = W[N]
for line in A:
    print(*line, sep='\t')
