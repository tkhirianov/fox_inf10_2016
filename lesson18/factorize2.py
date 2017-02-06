n = int(input())

print('n = 1', end='')
d = 2
while n != 1:
    k = 0
    while n%d == 0:
        k += 1
        n = n//d
    if k == 1:
        print('*', d, sep='', end='')
    elif k > 1:
        print('*', d, '^', k, sep='', end='')
    d += 1
