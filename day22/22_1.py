from dataclasses import dataclass

input_file = "input.txt"

@dataclass()
class Point:
    x: int
    y: int

def get_input():
    return open(input_file, 'r').read()

def main():
    lines = get_input().splitlines()
    depth = int(lines[0].split()[1])
    target = tuple(map(int, lines[1].split()[1].split(',')))
    target = Point(x=target[0], y=target[1])

    # define cave
    cave = []
    for y in range(target.y+1):
        cave.append([0] * (target.x + 1))

    # set mouth val
    cave[0][0] = 0  

    # set y=0 vals
    for x in range(target.x+1):
        cave[0][x] = x * 16807

    # set x=0 vals
    for y in range(target.y+1):
        cave[y][0] = y * 48271

    # set rest of the vals
    for y in range(1, target.y+1):
        for x in range(1, target.x+1):
            erosion_x = (cave[y][x-1] + depth) % 20183
            erosion_y = (cave[y-1][x] + depth) % 20183
            cave[y][x] = erosion_x * erosion_y

    type_map = {
        0: '.',
        1: '=',
        2: '|',
    }
    risk_level = 0
    for y in range(0, target.y+1):
        for x in range(0, target.x+1):
            if (x==0 and y==0) or (x==target.x and y==target.y):
                cave[y][x] = "X"
                continue
            erosion = (cave[y][x] + depth) % 20183
            risk_level += erosion % 3
            cave[y][x] = type_map[erosion%3]


    return risk_level

def print_cave(cave):
    for row in cave:
        str_row = list(map(str, row))
        print(''.join(str_row))

if __name__ == "__main__":
    print(main())
