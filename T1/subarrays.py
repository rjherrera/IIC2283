from random import randint

# BOTTOM UP

# ms(i) representa suma máxima hasta el indice i
# -> max { elegir el i: i + ms(i - 3), no elegir el i: ms(i - 1) }
# Formalmente:
# base: i = 0: elementos[0]
# base: i = 1: max(elementos[0], elementos[1])
# base: i = 2: max(elementos[0], elementos[1], elementos[2])
# recu: i > 2: max(elementos[i] + ms(i - 3), ms(i - 1))


def max_sum(n, elements):
    table = [None for i in range(n)]
    if n > 0:
        table[0] = elements[0]
    if n > 1:
        table[1] = max(table[0], elements[1])
    if n > 2:
        table[2] = max(table[1], elements[2])
    for i in range(3, n):
        table[i] = max(elements[i] + table[i - 3], table[i - 1])
    return table[-1]


if __name__ == '__main__':
    n = int(input())
    elements = [int(i) for i in input().split()]

    # input_text = '10\n61 72 24 12 61 7 59 47 46 51'
    # inputs = input_text.split('\n')
    # n, elements = int(inputs[0]), [int(i) for i in inputs[1].split()]

    print(max_sum(n, elements))
