import copy

from aoc2020.utils.input import read_input


def solution(update_seat_fn):
    data = read_input('input.txt')
    data = [list(d) for d in data]
    rows = len(data)
    columns = len(data[0])
    while True:
        new_seat_arrangement = copy.deepcopy(data)
        total_occupied_seats = 0
        for i in range(0, rows):
            for j in range(0, columns):
                new_seat_arrangement[i][j] = update_seat_fn(data, i, j, rows, columns)
                if new_seat_arrangement[i][j] == '#':
                    total_occupied_seats += 1
        if data == new_seat_arrangement:
            return total_occupied_seats
        data = new_seat_arrangement


def update_seat_occupancy(current_seat, adjacent_seats, empty_seats, occupied_seats, valid_occupied_seats):
    if current_seat == 'L':
        if empty_seats == adjacent_seats:
            return '#'
    elif current_seat == '#':
        if occupied_seats >= valid_occupied_seats:
            return 'L'
    return current_seat


def update_seat_part1(data, curr_row, curr_column, rows, columns):
    adjacent_seats, empty_seats, occupied_seats = 0, 0, 0
    adjacent_range = [-1, 0, 1]
    current_seat = data[curr_row][curr_column]
    for x in adjacent_range:
        for y in adjacent_range:
            adj_row = curr_row + x
            adj_column = curr_column + y
            if adj_row < 0 or adj_column < 0 or adj_row > (rows - 1) or adj_column > (columns - 1):
                continue
            adj_seat = data[adj_row][adj_column]
            if adj_row != curr_row or adj_column != curr_column:
                adjacent_seats += 1
                if adj_seat == 'L' or adj_seat == '.':
                    empty_seats += 1
                elif adj_seat == '#':
                    occupied_seats += 1
    return update_seat_occupancy(current_seat, adjacent_seats, empty_seats, occupied_seats, 4)


def update_seat_part2(data, curr_row, curr_column, rows, columns):
    adjacent_seats, empty_seats, occupied_seats = 0, 0, 0
    current_seat = data[curr_row][curr_column]
    adjacent_range = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for x, y in adjacent_range:
        adj_row = curr_row + x
        adj_column = curr_column + y
        while True:
            if adj_row < 0 or adj_column < 0 or adj_row > (rows - 1) or adj_column > (columns - 1):
                break
            adj_seat = data[adj_row][adj_column]
            if adj_seat == 'L':
                adjacent_seats += 1
                empty_seats += 1
                break
            elif adj_seat == '#':
                adjacent_seats += 1
                occupied_seats += 1
                break
            adj_row = adj_row + x
            adj_column = adj_column + y

    return update_seat_occupancy(current_seat, adjacent_seats, empty_seats, occupied_seats, 5)


def __main():
    print(solution(update_seat_part1))
    print(solution(update_seat_part2))


if __name__ == '__main__':
    __main()
