from typing import List

from aoc2020.utils.input import read_input

data = read_input('input.txt')
data = sorted([int(d) for d in data])
data = [0] + data + [data[-1] + 3]


def part1():
    curr = 0
    diff_one_counts = 0
    diff_three_counts = 1
    for i in data:
        diff = i - curr
        if diff == 1:
            diff_one_counts += 1
        elif diff == 3:
            diff_three_counts += 1
        curr = i
    return diff_one_counts * diff_three_counts


def is_valid_combo(i, j):
    return j - i <= 3


# recursion without memoization - not good for large inputs
def part2_without_memoization(d: List[int], idx: int):
    if idx >= len(data) - 1:
        return 1
    count = 0
    for r in range(1, 4):
        if (idx+r) >= len(data):
            break
        if is_valid_combo(data[idx], data[idx+r]):
            count += part2_without_memoization(d, idx + r)
    return count


existing = {}


def part2_with_memoization(idx: int):
    if idx in existing:
        return existing[idx]
    if idx >= len(data) - 1:
        existing[idx] = 1
        return 1
    count = 0
    for r in range(1, 4):
        if (idx + r) >= len(data):
            break
        if is_valid_combo(data[idx], data[idx + r]):
            count += part2_with_memoization(idx + r)
    existing[idx] = count
    return count


def __main():
    print(part1())
    print(part2_with_memoization(0))


if __name__ == '__main__':
    __main()
