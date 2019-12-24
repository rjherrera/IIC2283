from functools import reduce
from math import gcd


def egcd(a, b):
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    r0, r1 = b, a
    while r1 > 0:
        s0, s1 = s1, s0 - r0 // r1 * s1
        t0, t1 = t1, t0 - r0 // r1 * t1
        r0, r1 = r1, r0 % r1
    return r0, t0, s0


def lcm(a, b):
    return (a * b) // gcd(a, b)


# based on:
# https://forthright48.com/chinese-remainder-theorem-part-2-non-coprime-moduli/
# and https://math.stackexchange.com/a/1644698
def crt_two(a, b, m, n):
    g = gcd(m, n)
    mg, ng = m // g, n // g
    _, u, v = egcd(mg, ng)
    if (a - b) % g:
        return None
    # one solution is (a · n // g · v) + (b · m // g · u)
    # but the minimal one is that expression (mod LCM(m, n))
    return (a * ng * v + b * mg * u) % lcm(m, n)


def crt_generalized(remainders, moduli):
    r = remainders[0]
    m = moduli[0]
    for r_i, m_i in zip(remainders[1:], moduli[1:]):
        r = crt_two(r, r_i, m, m_i)
        m = lcm(m, m_i)
        if not r:
            return None
    return r


def simultaneous_encounter(N, M, K, agencies, people):
    cycles = [set() for _ in range(K)]
    visiting_order = [[] for _ in range(K)]
    visited_at_N = []
    # travel through nodes and check in each i if they all encounter
    # also detect cycles and visiting order
    for i in range(2 * N):
        for k in range(K):
            c, a = people[k]
            agency = agencies[a - 1]
            new_city = agency[c - 1]
            people[k] = [new_city, a]
            visiting_order[k].append(new_city)
            if i == N - 1:
                visited_at_N.append(new_city)
            elif i >= N:
                cycles[k].add(new_city)
        cities = list(map(lambda x: x[0], people))
        if cities.count(cities[0]) == len(cities):
            return cities[0], i + 1

    # if they did not encounter they will not be able to do so if
    # their cycles do not intersect
    inter = reduce(lambda x, y: x.intersection(y), cycles)
    if inter == set():
        return '*'

    # get cycles ordered by time of visiting
    ordered_cycles = [[] for _ in range(K)]
    for k in range(K):
        cycle = []
        for i in visiting_order[k]:
            if i in cycles[k] and i not in ordered_cycles[k]:
                ordered_cycles[k].append(i)

    # deduce equations of the form T = A[k] (mod C[k]) for each k
    # to be able to solve them using the chinese remainder theorem
    # where A[k] = RX[k] - RN[k] + N, RX[k] is the index of node X in the cycle
    # and RN[k] is the index of node at T=N in the cycle
    C = [len(i) for i in cycles]
    RN = [i.index(j) for i, j in zip(ordered_cycles, visited_at_N)]
    encounters = []
    for x in inter:
        RX = [i.index(x) for i in ordered_cycles]
        A = [RX[k] - RN[k] + N for k in range(K)]
        encounters.append([x, crt_generalized(A, C)])
        # append city x and time of encounter (solution to the CRT)
    if set(map(lambda x: x[1], encounters)) == set([None]):
        return '*'
    real_encounters = filter(lambda x: x[1] is not None, encounters)
    return min(real_encounters, key=lambda x: x[1])


if __name__ == '__main__':
    N, M, K = [int(i) for i in input().split()]
    agencies = [[int(i) for i in input().split()] for _ in range(M)]
    people = [[int(i) for i in input().split()] for _ in range(K)]

    print(*simultaneous_encounter(N, M, K, agencies, people))
