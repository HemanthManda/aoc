import sys
from functools import reduce
from operator import mul

from aoc2020.utils.input import read_input

data = read_input('input.txt')


def part1():
    timestamp = int(data[0])
    bus_ids = [int(d) for d in data[1].split(',') if d != 'x']
    min_val, min_bus_id = sys.maxsize, -1
    for i in bus_ids:
        next_sch = timestamp + (i - (timestamp % i))
        if next_sch < min_val:
            min_val = next_sch
            min_bus_id = i
    return (min_val - timestamp) * min_bus_id


def build_numbers_and_remainders():
    """
    if N is the final number we are looking for
    build num[] and rem[] such that N % num[i] = rem[i]
    """
    num, rem = [], []
    for idx, i in enumerate(data[1].split(',')):
        if i != 'x':
            i = int(i)
            num.append(i)
            if idx == 0:
                rem.append(0)
            elif idx > i:
                rem.append(i - (idx % i))
            else:
                rem.append(i - idx)
    return num, rem


def calc_inv_modulo(numbers, product_of_remaining):
    inv_modulo = []
    for idx, i in enumerate(numbers):
        n = 1
        while True:
            if (product_of_remaining[idx] * n) % i == 1:
                inv_modulo.append(n)
                break
            n += 1
    return inv_modulo


# chinese remainder theorem
def part2():
    numbers, remainders = build_numbers_and_remainders()
    product = reduce(mul, numbers, 1)
    product_of_remaining = [int(product/i) for i in numbers]
    inv_modulo = calc_inv_modulo(numbers, product_of_remaining)

    s = 0
    for idx, i in enumerate(remainders):
        s += remainders[idx] * product_of_remaining[idx] * inv_modulo[idx]
    return s % product


def __main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    __main()
