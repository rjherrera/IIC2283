from cmath import exp, pi


def closest_power_of_2(n):
    return 1 << (n - 1).bit_length()


def enlarge(array, n, item=0):
    return array + [item] * (n - len(array))


def fft(n, a):
    if n == 4:
        w_1 = exp(pi / n * -2j)
        a0, a1, a2, a3 = a
        return [a0 + a2 + a1 + a3,
                a0 - a2 + w_1 * (a1 - a3),
                a0 + a2 - a1 - a3,
                a0 - a2 - w_1 * (a1 - a3)]
    elif n == 2:
        return [a[0] + a[1], a[0] - a[1]]

    half = n // 2
    y_even = fft(half, a[0::2])
    y_odd = fft(half, a[1::2])
    y = [None] * n

    pi_2j_over_n = pi / n * -2j
    for k in range(half):
        x = exp(pi_2j_over_n * k) * y_odd[k]
        y_even_k = y_even[k]
        y[k] = y_even_k + x
        y[half + k] = y_even_k - x
    return y


def product(p, q):
    n_p, n_q = len(p), len(q)
    size = 2 * closest_power_of_2(max(n_p, n_q))
    new_p = enlarge(p, size)
    new_q = enlarge(q, size)

    y = fft(size, new_p)
    z = fft(size, new_q)

    unordered_pre_prod = [i * j for i, j in zip(y, z)]
    pre_prod = unordered_pre_prod[:1] + unordered_pre_prod[:0:-1]

    prod = [round((i / size).real) for i in fft(size, pre_prod)]
    return prod[:n_p + n_q - 1]


if __name__ == '__main__':
    # with open('Tarea2_ejemplos_input_output/p2_in.txt') as f:
    #     input_p = f.readline().strip()
    #     input_q = f.readline().strip()

    p_degree, *p = [int(i) for i in input().split()]
    q_degree, *q = [int(i) for i in input().split()]

    answer = product(p, q)
    print(p_degree + q_degree, str(answer).replace(',', '')[1:-1])
