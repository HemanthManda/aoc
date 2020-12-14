import itertools
import re

from aoc2020.utils.input import read_input

data = read_input('input.txt')

CHAR_LENGTH = 36


def int_to_bin(num: int):
    return bin(num).replace('0b', '').zfill(CHAR_LENGTH)


def process_with_mask(mask, value, mask_char):
    value_after_mask = [v if m == mask_char else m for m, v in zip(mask, value)]
    return ''.join(value_after_mask)


def part1():
    mask = ''
    memory = {}
    for line in data:
        if 'mask' in line:
            mask = line.replace('mask = ', '')
        else:
            [key, value] = [li.strip() for li in line.split('=')]
            value = int_to_bin(int(value))
            value_after_mask = process_with_mask(mask, value, 'X')
            memory[key] = int(value_after_mask, 2)
    return sum(memory.values())


def part2():
    mask = ''
    memory = {}
    for line in data:
        if "mask" in line:
            mask = line.replace('mask = ', '')
        else:
            [key, value] = line.split('=')
            key = re.findall(r'\d+', key)[0]
            key = int_to_bin(int(key))
            key_after_mask = process_with_mask(mask, key, '0')
            memory[key_after_mask] = value.strip()

    updated_memory = {}
    for key, val in memory.items():
        all_possible_vals = itertools.product([0, 1], repeat=key.count('X'))
        # this might be really slow
        # what's a better way to replace occurrences of same characters with different characters from a list?
        for idx, v in enumerate(all_possible_vals):
            curr = 0
            curr_val = list(key)
            for curr_idx, i in enumerate(curr_val):
                if i == 'X':
                    curr_val[curr_idx] = str(v[curr])
                    curr += 1
            updated_memory[''.join(curr_val)] = int(val)
    return sum(updated_memory.values())


def __main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    __main()
