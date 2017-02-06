x = int(input())

d = 2
while d*d <= x:
    if x%d == 0:  # d - нетривиальный делитель
        print('число составное')
        break
    d += 1
else:
    print('число простое')

