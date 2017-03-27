def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1)*n


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def pow(a, n):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return pow(a, n-1)*a
    else:
        return pow(a**2, n//2)


a = int(input("a = "))
print("factorial(a) =", factorial(a))
b = int(input("b = "))
print('gcd(a, b) =', gcd(a, b))
print('pow(a, b) =', pow(a, b))
