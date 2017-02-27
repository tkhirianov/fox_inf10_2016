N = int(input())
Q = [int(input()) for i in range(7)]
current = 0
max_left = -10**10
max_sum = max_left*2
for i in range(N-7):
    x = int(input())
    max_left = max(max_left, Q[current])
    if x + max_left > max_sum:
        max_sum = x + max_left
    Q[current] = x
    current = (current + 1)%7
    
print(max_sum)
