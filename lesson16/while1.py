print(*range(4, 100, 3))
print("Арифметическая прогрессия:")
x = 4  # start
while x < 100:  # stop
    print(x, end=' ')
    x += 3  # step
print()
print("Геометрическая прогрессия:")
x = 2  # start
while x < 100:  # stop
    print(x, end=' ')
    x *= 3  # step
print()

x = 123
print('Цифры числа', x, end=':\n')
while x != 0:
    digit = x%2
    print(digit)
    x = x//2
