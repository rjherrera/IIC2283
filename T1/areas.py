from random import randint


def area(a, b):
    return (b[0] - a[0]) * (b[1] - a[1])


def max_area(A, B):
    if not len(A) or not len(B):
        return 0

    n = len(A)
    n_dots = n // 2
    middle = n_dots - (2 - n_dots % 2)
    a_middle = A[middle], A[middle + 1]

    middle_best = 0
    max_j = -1
    for j in range(0, len(B), 2):
        b = B[j], B[j + 1]
        x = area(b, a_middle)
        if middle_best < x:
            middle_best = x
            max_j = j
    # se descartan los cruzados (left with right, right with left)
    # porque ahí no puede estar el máximo, tomando como separador
    # de A su punto medio, 'a', y de B el de area maxima para 'a'
    left_with_left = max_area(A[:middle], B[:max_j + 2])
    right_with_right = max_area(A[middle + 2:], B[max_j:])

    return max(middle_best, left_with_left, right_with_right)


if __name__ == '__main__':
    n = int(input())
    A, B = ([int(i) for i in j.split()] for j in [input(), input()])

    # input_text = '5\n1 6 3 5 4 4 5 2 6 0\n7 13 8 12 11 11 12 8 13 7'
    # input_text = '4\n-3 4 -1 1 3 -1 4 -2\n4 9 6 8 7 7 9 6'
    # input_text = '3\n-3 4 -1 1 3 -1\n4 9 6 8 7 7'
    # ins = input_text.split('\n')
    # n, [A, B] = int(ins[0]), [[int(i) for i in j.split()] for j in ins[1:3]]

    print(max_area(A, B))
