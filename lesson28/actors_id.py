max_actors_number = 10
N = int(input())
rating = {}
for sms in range(N):
    actor = input()
    rating[actor] = rating.get(actor, 0) + 1

A = [(actor, rating[actor]) for actor in rating]
for pos in range(0, len(A)-1):
    for i in range(pos, len(A)):
        if A[i][1] > A[pos][1]:
            A[i], A[pos] = A[pos], A[i]

for i in range(len(A)):
    print(*A[i])
