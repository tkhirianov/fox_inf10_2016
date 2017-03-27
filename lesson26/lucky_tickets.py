def count_lucky_tickets1(N=6):
    assert N%2 == 0, 'Число должно быть чётным!'
    count = 0
    for a in range(0, 10**(N//2)):
        a_sum = sum(int(digit) for digit in list(str(a)))
        for b in range(0, 10**(N//2)):
            b_sum = sum(int(digit) for digit in list(str(b)))
            if b_sum == a_sum:
                # print(a, b, sep=' ')  # DEBUG PRINT
                count += 1
    print("Количество счастливых билетов:", count)

count_lucky_tickets1(6)
