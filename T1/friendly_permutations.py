from math import ceil, factorial


def ncr(n, r):
    if n - r < 0:
        return 1
    return factorial(n) // (factorial(r) * factorial(n - r))


def friendly_naive(n):
    N = len(n)
    F = [n.count(str(i)) for i in range(10)]
    P = ceil(N / 2)  # mandando ceil(N/2) a los pares

    DP = [[[0 for _ in range(11)] for _ in range(P + 1)] for _ in range(11)]
    DP[10][0][0] = 1

    # como repartir digitos a P posiciones pares y a I posiciones impares
    for k in range(9, -1, -1):
        f_k = F[k]
        f_no_k = sum(F[i] for i in range(k, 10))
        # poniendo el digito k -> me quedan por poner todos los digitos >= k
        for p in range(P + 1):
            for x in range(11):
                for z in range(min(f_k, p) + 1):
                    # z = to_even -> de los que puedo repartir, cuantos a pares
                    even_addition = z * k  # lo que agrego a la suma de pares
                    odd_addition = (f_k - z) * k  # ''' a la suma de de impares
                    change = even_addition - odd_addition

                    new_p = p - z  # p: cuantos en pos par me quedan por poner
                    new_x = (x + change) % 11  # resto: antiguo + el cambio %11

                    to_even = z  # cuantos numeros k se van a pares
                    to_odd = f_k - z  # cuantos numeros k se van a pares

                    ways_of_even = ncr(p, to_even)
                    ways_of_odd = ncr(f_no_k - p, to_odd)
                    # f_no_k - p: los que me quedan por poner tras poner los p
                    next_dp = DP[k + 1][new_p][new_x]
                    DP[k][p][x] += ways_of_even * ways_of_odd * next_dp
    return DP[0][P][0]


def friendly_permutations(n):
    if '0' in n:
        x = friendly_naive(n) - friendly_naive(n.replace('0', '', 1))
    else:
        x = friendly_naive(n)
    return x % (10 ** 9 + 7)


if __name__ == '__main__':
    n = input()
    print(friendly_permutations(n.strip()))

    # print(friendly_permutations('5515845699623518795907565227954004945714084733679096084426543411117671412753101421942301615665384863'))
    # print(friendly_permutations('73251455528701'))
    # print(friendly_permutations('768576958'))
    # print(friendly_permutations('209000'))
    # print(friendly_permutations('20900'))
    # print(friendly_permutations('2090'))
    # print(friendly_permutations('835'))
    # print(friendly_permutations('132'))
    # print(friendly_permutations('11'))
    # print(friendly_permutations('2'))
