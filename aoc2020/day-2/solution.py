from aoc2020.utils.input import read_input

data = read_input('input.txt')
data = [d.split(' ') for d in data]


def process_input(input_data):
    password = input_data[2]
    char_to_check = input_data[1].split(':')[0]
    min_max = input_data[0].split('-')
    valid_min, valid_max = int(min_max[0]), int(min_max[1])
    return password, char_to_check, valid_min, valid_max


def count_valid_passwords_scenario_1():
    valid_passwords_count = 0
    for d in data:
        password, char_to_check, valid_min, valid_max = process_input(d)
        char_count = 0
        for char in password:
            if char == char_to_check:
                char_count += 1
        if valid_min <= char_count <= valid_max:
            valid_passwords_count += 1
    return valid_passwords_count


def count_valid_passwords_scenario_2():
    valid_passwords_count = 0
    for d in data:
        password, char_to_check, first_index, second_index = process_input(d)
        password_characters = list(password)
        if (password_characters[first_index - 1] == char_to_check) ^ \
                (password_characters[second_index - 1] == char_to_check):
            valid_passwords_count += 1
    return valid_passwords_count


def __main():
    print(count_valid_passwords_scenario_1())
    print(count_valid_passwords_scenario_2())


if __name__ == '__main__':
    __main()
