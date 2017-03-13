def find_abcd(s):
    state = 0
    for char in s:
        if state == 0:
            if char == 'a':
                state = 1
        elif state == 1:
            if char == 'b':
                state = 2
            elif char == 'a':
                state = 1
            else:
                state = 0
        elif state == 2:
            if char == 'c':
                state = 3
            elif char == 'a':
                state = 1
            else:
                state = 0
        elif state == 3:
            if char == 'd':
                state = 4
            elif char == 'a':
                state = 1
            else:
                state = 0
        elif state == 4:
            return True
        print(char, state)

    return False
