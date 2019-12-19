from math import floor, ceil, log2
from random import randint


def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        return gcd(b, a % b)
    return gcd(a, b % a)


def exp(n, k):
    if k == 1:
        return n
    if k % 2 == 0:
        val = exp(n, k // 2)
        return val * val
    val = exp(n, (k - 1) // 2)
    return val * val * n


def exp_mod(a, b, n):
    if b == 1:
        return a % n
    if b % 2 == 0:
        val = exp_mod(a, b // 2, n)
        return (val * val) % n
    val = exp_mod(a, (b - 1) // 2, n)
    return (val * val * a) % n


def has_integer_root(n, k, i, j):
    if i == j:
        return exp(i, k) == n
    if i < j:
        p = floor((i + j) // 2)
        val = exp(p, k)
        if val == n:
            return True
        if val < n:
            return has_integer_root(n, k, p + 1, j)
        return has_integer_root(n, k, i, p - 1)
    return False


def is_power(n):
    if n <= 3:
        return False
    for k in range(2, ceil(log2(n))):
        if has_integer_root(n, k, 1, n):
            return True
    return False


def small_prime(n):
    return n in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


# based on
# http://marenas.sitios.ing.uc.cl/iic2283-19/clases/alg_teoria_numeros-2-imp.pdf#page=31
def prime(n):
    if n < 50:
        return small_prime(n)
    if n % 2 == 0:
        return False
    if is_power(n):
        return False

    k = 20  # para que la prob de error sea 1/2^20 ya que es 1/2^k
    a = [randint(1, n - 1) for _ in range(k)]
    b = [0] * k
    for i in range(min(n - 1, k)):
        if gcd(a[i], n) > 1:
            return False
        b[i] = exp_mod(a[i], (n - 1) // 2, n)
    neg = 0
    for i in range(k):
        if b[i] % n == -1 % n:
            neg += 1
        elif b[i] % n != 1:
            return False
    return neg != 0


if __name__ == '__main__':
    n = int(input())
    print('YES' if prime(n) else 'NO')
