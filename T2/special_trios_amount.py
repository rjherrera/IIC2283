from numpy.fft import fft, ifft


def closest_power_of_2(n):
    return 1 << (n - 1).bit_length()


def enlarge(array, n, item=0):
    return array + [item] * (n - len(array))


def product(p, q):
    n_p, n_q = len(p), len(q)
    size = 2 * closest_power_of_2(max(n_p, n_q))

    new_p = enlarge(p, size)
    new_q = enlarge(q, size)

    prod = [int(round(i.real)) for i in ifft(fft(new_p) * fft(new_q))]
    while prod and prod[-1] == 0:
        prod.pop()
    return prod


def special_trios_amount(n, a):
    m = min(a)
    x = [0] * (max(a) + 1 - m)
    for i in range(n):
        x[a[i] - m] += 1

    y = product(x, x)
    # restar los tripletes (i, i, 2i)
    for i in range(len(y)):
        if i % 2 == 0:
            y[i] -= x[i // 2]
    if 0 >= m:
        zeroes = x[0 - m]
        # restar los tripletes (j, 0, j) y (0, j, j)
        for i in range(len(y)):
            if i != 0 - 2 * m:
                y[i] -= 2 * zeroes
        # restar los tripletes (i, i, i) con i = 0
        if zeroes > 1:
            y[0 - 2 * m] -= 2 * (zeroes - 1)
    return sum(y[i - 2 * m] for i in a if i >= m)


if __name__ == '__main__':
    # with open('Tarea2_ejemplos_input_output/p3_in.txt') as f:
    #     input_n = f.readline().strip()
    #     input_a = f.readline().strip()

    n = int(input())
    a = [int(i) for i in input().split()]

    print(special_trios_amount(n, a))
