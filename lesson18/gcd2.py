a = int(input())
b = int(input())
while a != 0 and b != 0:
    if a > b:
        a = a%b
    else:
        b = b%a
if a == 0:
    print(b)
else:
    print(a)
