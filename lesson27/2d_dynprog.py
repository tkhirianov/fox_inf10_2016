M = int(input('M='))
N = int(input('N='))

K = [[0]*(M+1), [0] + [1]*(M)] + [[0] + [None]*M for i in range(N-1)]
for i in range(2, N+1):
    for j in range(1, M+1):
        K[i][j] = K[i-1][j] + K[i][j-1]

print('Количество способов попасть в точку (M, N):', K[N][M])
print('Матрица K:')
for line in K:
    print(*line, sep='\t')
