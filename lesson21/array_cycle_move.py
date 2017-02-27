def move_left(A):
    tmp = A[0]
    for i in range(len(A)-1):
        A[i] = A[i+1]
    A[-1] = tmp

def move_right(A):
    tmp = A[-1]
    for i in range(len(A)-2, -1, -1):
        A[i+1] = A[i]
    A[0] = tmp

A = list(range(10))
print(A)
for i in range(10):
    move_left(A)
    print(A)
for i in range(10):
    move_right(A)
    print(A)
