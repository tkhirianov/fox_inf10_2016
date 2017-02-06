from random import randint 

x = int(input())

a = randint(2, x-1)
if a**(x-1)%x == 1:
    print('число x вероятно простое')
else:
    print('число составное')

is_prime = True
d = 2
while d*d <= x:
    if x%d == 0:  # d - нетривиальный делитель
        is_prime = False
        break
    d += 1


if is_prime:
    print('число простое')
else:
    print('число составное')
