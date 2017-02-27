right_bracket = {'[': ']', '(': ')', '{': '}'}
Q = []

s = input()
correct = True
for bracket in s:
    if bracket in ['[', '(', '{']:
        Q.append(bracket)
    elif bracket in [']', ')', '}']:
        if len(Q) == 0:
            correct = False
            break
        other = Q.pop()
        if right_bracket[other] != bracket:
            correct = False
            break
else:
    correct = (len(Q) == 0)

print(correct)
