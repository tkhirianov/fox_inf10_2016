def matryoshka(n):
    if n == 1:
        print('  матрёшка размера 1')
    else:
        print('  '*n + 'верх матрёшки размера', n)
        matryoshka(n-1)
        print('  '*n + 'низ матрёшки размера', n)

matryoshka(5)
