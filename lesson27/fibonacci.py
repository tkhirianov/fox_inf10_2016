import time

def fib_recurse(n):
    if n == 1 or n == 0:
        return n
    return fib_recurse(n-1) + fib_recurse(n-2)

def fib_dynamic(n):
    fib = [None]*(n+1)
    fib[0] = 0
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

n = int(input("Введите n:"))
t0 = time.clock()
f1 =  -1 #fib_recurse(n)
t1 = time.clock()
print('Время рекуррентного счёта:', t1-t0)
t0 = time.clock()
f2 = fib_dynamic(n)
t2 = time.clock()
print('Время счёта динамическим программированием:', t2-t0)
print('Вычисленные числа:', f1, f2)
