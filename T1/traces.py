import sys

sys.setrecursionlimit(6000)


def traces(n, heights):
    if n == 0 or heights.count(0) == n:
        return 0
    m = min(heights)
    ix = heights.index(m)
    new = [i - m for i in heights]
    return min(n, m + traces(ix, new[:ix]) + traces(n - ix - 1, new[ix + 1:]))


if __name__ == '__main__':
    n = int(input())
    elements = [int(i) for i in input().split()]

    # input_text = '7\n2 4 3 6 4 2 1'
    # inputs = input_text.split('\n')
    # n, elements = int(inputs[0]), [int(i) for i in inputs[1].split()]

    print(traces(n, elements))
