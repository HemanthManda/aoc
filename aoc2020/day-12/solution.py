from aoc2020.utils.input import read_input

data = read_input('input.txt')

compass = {
    'N': ['W', 'E', 'S'],
    'E': ['N', 'S', 'W'],
    'S': ['E', 'W', 'N'],
    'W': ['S', 'N', 'E']
}

directions = compass.keys()


def get_updated_location(action, value, east, north):
    if action == 'N':
        north += value
    elif action == 'S':
        north -= value
    elif action == 'E':
        east += value
    elif action == 'W':
        east -= value
    return east, north


def get_updated_direction(action, value, direction):
    if action == 'L':
        if value == 90:
            direction = compass[direction][0]
        elif value == 270:
            direction = compass[direction][1]
        else:
            direction = compass[direction][2]
    elif action == 'R':
        if value == 90:
            direction = compass[direction][1]
        elif value == 270:
            direction = compass[direction][0]
        else:
            direction = compass[direction][2]
    return direction


def get_location_part1(action, value, east, north, direction):
    if action == 'F':
        east, north = get_updated_location(direction, value, east, north)
    elif action in directions:
        east, north = get_updated_location(action, value, east, north)
    else:
        direction = get_updated_direction(action, value, direction)
    return east, north, direction


def get_updated_path(action, value, waypoint_east, waypoint_north):
    east, north = waypoint_east, waypoint_north
    rotation = 1 if action == 'L' else -1
    if value == 90:
        waypoint_north = rotation * east
        waypoint_east = rotation * -north
    elif value == 270:
        waypoint_north = rotation * -east
        waypoint_east = rotation * north
    else:
        waypoint_east = -east
        waypoint_north = -north
    return waypoint_east, waypoint_north


def get_location_part2(action, value, east, north, waypoint_east, waypoint_north):
    if action == 'F':
        east += waypoint_east * value
        north += waypoint_north * value
    elif action in directions:
        waypoint_east, waypoint_north = get_updated_location(action, value, waypoint_east, waypoint_north)
    else:
        waypoint_east, waypoint_north = get_updated_path(action, value, waypoint_east, waypoint_north)
    return east, north, waypoint_east, waypoint_north


def part1():
    east, north = 0, 0
    direction = 'E'
    for direc in data:
        action, value = direc[0], int(direc[1:])
        east, north, direction = get_location_part1(action, value, east, north, direction)
    return abs(east) + abs(north)


def part2():
    east, north = 0, 0
    waypoint_east, waypoint_north = 10, 1
    for direction in data:
        action, value = direction[0], int(direction[1:])
        east, north, waypoint_east, waypoint_north = get_location_part2(action, value, east, north, waypoint_east, waypoint_north)
    return abs(east) + abs(north)


def __main():
    print(part1())
    print(part2())
    pass


if __name__ == '__main__':
    __main()
