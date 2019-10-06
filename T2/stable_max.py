def stable_max(n, na, nb, a, b, fa, fb):
    aa = sorted(a, key=lambda x: -(fa[x - 1] + fb[x - 1]))
    bb = sorted(b, key=lambda x: -(fa[x - 1] + fb[x - 1]))

    S = range(1, n + 1)
    better_a = sorted(S, key=lambda x: -fa[x - 1])
    better_b = sorted(S, key=lambda x: -fb[x - 1])
    better_c = sorted(S, key=lambda x: -(fa[x - 1] + fb[x - 1]))

    ta = set(a)
    i = 0
    while len(ta) < 2 * na and i < n:
        ta.add(better_a[i])
        i += 1

    tb = set(b)
    i = 0
    while len(tb) < 2 * nb and i < n:
        tb.add(better_b[i])
        i += 1

    if na <= nb:
        tc = set(a)
        x = na - len(tc & set(b))
        i = 0
        added = 0
        while added < x and i < nb:
            if bb[i] not in tc:
                tc.add(bb[i])
                added += 1
            i += 1
    else:
        tc = set(b)
        x = nb - len(tc & set(a))
        i = 0
        added = 0
        while added < x and i < na:
            if aa[i] not in tc:
                tc.add(aa[i])
                added += 1
            i += 1

    sa = set(a)
    sb = set(b)
    cnt_a = len(tc & sa)
    cnt_b = len(tc & sb)
    i = 0
    while len(tc) < 2 * cnt_a and len(tc) < 2 * cnt_b and i < n:
        x = better_c[i]
        if x not in tc:
            if x in sa:
                cnt_a += 1
            if x in sb:
                cnt_b += 1
            tc.add(x)
        i += 1

    Fta = sum(fa[i - 1] for i in ta)
    Ftb = sum(fb[i - 1] for i in tb)
    Ftc = sum(fa[i - 1] + fb[i - 1] for i in tc)

    if len(tc & sa) >= len(tc) / 2 and len(tc & sb) >= len(tc) / 2:
        return max(Fta, Ftb, Ftc)
    return max(Fta, Ftb)


if __name__ == '__main__':
    n, na, nb = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    fa = [int(i) for i in input().split()]
    fb = [int(i) for i in input().split()]

    print(stable_max(n, na, nb, a, b, fa, fb))
