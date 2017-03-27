def gen_m(N, M, prefix=""):
    """ Распечатывает все последовательности длины N из чисел от 0 до M-1,
        предваряя их префиксом prefix"""
    if N == 0:
        print(prefix)
    else:
        for x in range(0, M):
            gen_m(N-1, M, prefix + ' ' + str(x))


def gen_2(N, prefix=""):
    if N == 0:
        print(prefix)
    else:
        gen_2(N-1, prefix + '0')
        gen_2(N-1, prefix + '1')


def permutations(N, A=None):
    """ Генерирует и распечатывает все перестановки чисел от 0 до N-1
        A - список чисел, который будет дополнен до длины N
        оставшимися возможными числами
    """
    if A is None:
        A = []
    if len(A) == N:
        print(*A)
    else:
        for x in range(N):
            if x not in A:
                permutations(N, A + [x])


def permutations_m(N, M, A=None):
    """ Генерирует и распечатывает все перестановки чисел от 0 до M-1
        из N таких чисел
        A - список чисел, который будет дополнен до длины N
        оставшимися возможными числами
    """
    if A is None:
        A = []
    if N == 0:
        print(*A)
    else:
        for x in range(M):
            if x not in A:
                permutations_m(N-1, M, A + [x])


permutations_m(3, 4)
