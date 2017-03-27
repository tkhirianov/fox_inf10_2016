def gen_specific_disposition(N, prefix=""):
    if N == 0:
        print(prefix)
    else:
        if len(prefix) > 0 and prefix[-1] == '1':
            gen_specific_disposition(N-1, prefix+'0')
        else:
            gen_specific_disposition(N-1, prefix + '0')
            gen_specific_disposition(N-1, prefix + '1')


def generate_subsets(A, mask = None):
        if mask is None:
            mask = []
        if len(A) == len(mask):
            for element, condition in zip(A, mask):
                if condition:
                    print(element, end =' ')
            print()
        else:
            generate_subsets(A, mask+[1])
            generate_subsets(A, mask+[0])

generate_subsets(['A', 'B', 'C'])

#gen_specific_disposition(5)
