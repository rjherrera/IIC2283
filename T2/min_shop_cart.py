import heapq


def enlarge(array, n, item=0):
    return array + [item] * (n - len(array))


def min_shop_cart(n, I, B):
    m = len(B[0])
    for i in B:
        m = max(len(i), m)
    heap = []
    for i in B:
        heap.append(enlarge(i[::-1], m, item=I))
    heapq.heapify(heap)

    T = sum(len(i) for i in B)
    order = []
    for i in range(T):
        shelf = heapq.heappop(heap)
        order.append(shelf.pop(0))
        shelf.append(I)
        if shelf:
            heapq.heappush(heap, shelf)

    r = 0
    cI = I
    for i in reversed(order):
        r = r + i * cI
        cI = cI * I
    return r % (10 ** 9 + 7)


if __name__ == '__main__':
    # with open('Tarea2_ejemplos_input_output/p4_in.txt') as f:
    #     input_ni = f.readline().strip()
    #     input_b = []
    #     for i in range(int(input_ni.split()[0])):
    #         input_b.append(f.readline().strip())
    # n, I = [int(i) for i in input().split()]
    # B = [[int(j) for j in i.split()[1:]] for i in input_b]

    n, I = [int(i) for i in input().split()]
    B = [[int(i) for i in input().split()[1:]] for _ in range(n)]

    print(min_shop_cart(n, I, B))
