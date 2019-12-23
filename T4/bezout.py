# based on
# http://marenas.sitios.ing.uc.cl/iic2283-19/clases/alg_teoria_numeros-1-imp.pdf#page=24
def egcd(a, b):
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    r0, r1 = b, a
    while r1 > 0:
        s0, s1 = s1, s0 - r0 // r1 * s1
        t0, t1 = t1, t0 - r0 // r1 * t1
        r0, r1 = r1, r0 % r1
    return r0, t0, s0


def diophantine(s, t, m):  # use egcd(s,t) to get s·x + t·y = gcd
    gcd, x, y = egcd(s, t)
    factor = m // gcd
    return gcd, x * factor, y * factor  # amplify to get s·x' + t·y' = m


def bezout_numbers(s, t, m):
    gcd, x0, y0 = diophantine(s, t, m)  # candidate for s·a + t·b = m (not min)
    x_generalizer = -t // gcd
    y_generalizer = s // gcd

    # choose n to get minimum diophantine solution for s·a + t·b = m
    # as general diphantine sol: x = x0 - t // gcd · n, y = y0 + s // gcd · n
    n = min(abs(x0 // x_generalizer), abs(y0 // y_generalizer))

    if x0 > 0 and y0 > 0:
        n = -n
        while x0 + n * x_generalizer > 0 and y0 + n * y_generalizer > 0:
            n -= 1
    else:
        while x0 + n * x_generalizer <= 0 or y0 + n * y_generalizer <= 0:
            n += 1

    if n < 0:  # in the first case 1 unnecesary step is done (and x gets <= 0)
        n += 1
    return x0 + n * x_generalizer, y0 + n * y_generalizer


if __name__ == '__main__':
    s, t, m = [int(i) for i in input().split()]
    print(*bezout_numbers(s, t, m))
