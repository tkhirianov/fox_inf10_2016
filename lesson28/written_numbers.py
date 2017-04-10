numbers = list(range(1, 10)) + list(range(11, 20)) + list(range(10, 100, 10))
numbers_by_name = {input(): x for x in numbers}
s = 0
N = int(input())
for k in range(N):
    x = 0
    line = input()
    for word in line.split():
        if word in numbers_by_name:
            x += numbers_by_name[word]
        else:
            x = 0  # недопустимое число!
            break
    s += x
print(s)
