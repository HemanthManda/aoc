from aoc2020.utils.input import read_input

data = read_input('input.txt')


def product_of_sum_of_two(final_sum: int):
    processed = {}
    for current in data:
        remaining = final_sum - int(current)
        if remaining in processed:
            return current * remaining
        processed[current] = remaining
    return 0


def product_of_sum_of_three(final_sum: int):
    processed_for_two = {}
    for d in data:
        processed_for_two[d] = final_sum - int(d)
    for k, v in processed_for_two.items():
        processed_for_three = {}
        for current in data:
            if current != k:
                remaining = v - int(current)
                if remaining in processed_for_three:
                    return k * int(current) * remaining
                processed_for_three[current] = remaining
    return 0


def __main():
    print(product_of_sum_of_two(2020))
    print(product_of_sum_of_three(2020))


if __name__ == '__main__':
    __main()
