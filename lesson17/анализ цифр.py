x = int(input())
m = 10

while x > 0:
    if x%10 < m:
        m = x%10

    x //= 10

if m == 10:
    print('цифр в числе нет')
else:
    print(m)
