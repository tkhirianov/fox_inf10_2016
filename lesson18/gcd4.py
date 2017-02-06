a = int(input())
b = int(input())
while b != 0:
    a, b = b, a%b  # a > b
print(a)
