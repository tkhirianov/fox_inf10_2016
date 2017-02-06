x = 2
step = 4
N = int(input())

n = 0
s = 0
f = True

for i in range(N):
    print(x)
    n += 1
    s += x
    f = f and x%2 == 0
    
    x += step

print('Всего было n =', n, 'чётных элементов')
print('Сумма чётных элементов s = ', s)
print('Среднее арифметическое чётных:', s/n)
print('f = ', f)
