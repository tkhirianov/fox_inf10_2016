def check_sort(sort):
    """ возвращает результат ОК/Fail"""

    test_cases = []
    # test_case 1
    test_cases.append((1, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
    test_cases.append((2, [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]))
    test_cases.append((3, [1, 3, 2, 5, 4], [1, 2, 3, 4, 5]))
    test_cases.append((4, [1, 2, 1, 1, 2], [1, 1, 1, 2, 2]))
    test_cases.append((5, [1, 3, 10, 11, 8, 5, 7, 2, 13, 12, 9, 6, 4, 14],
                       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))

    check_result = 'OK'
    for i, A, R in test_cases:
        if R == sort(A[:]):
            print('\ttest case ', i, ': OK')
        else:
            print('\ttest case ', i, ': Fail')
            check_result = 'Fail'
    return check_result


def monkey_sort(A):
    """ сортировка обезьяны. O(N!) """
    from random import shuffle
    while A != sorted(A):
        shuffle(A)
    return A


def choice_sort(A):
    """ сортировка выбором минимума """
    N = len(A)
    for pos in range(0, N-1):
        for i in range(1, N):
            if A[i] < A[pos]:
                A[i], A[pos] = A[pos], A[i]
    return A


def insert_sort(A):
    """ insert_sort """
    N = len(A)
    for k in range(1, N):
        i = k
        while i > 0 and A[i] < A[i-1]:
            A[i], A[i-1] = A[i-1], A[i]
            i -= 1
    return A


def bubble_sort(A):
    """ bubble_sort """
    N = len(A)
    for bypass in range(1, N):
        for i in range(0, N-bypass):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
    return A


if __name__ == '__main__':
    for sort in choice_sort, insert_sort, bubble_sort, monkey_sort:
        print('Test', sort.__doc__, ':')
        result = check_sort(sort)
        print('Test', sort.__doc__, '-', result)
        print()
