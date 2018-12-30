import re
from copy import deepcopy

input_file = "input.txt"

def get_input():
    return open(input_file, 'r').read()

class Line:
    def __init__(self, line):
        split = re.split(',| |=|\.', line)
        self.fixed_char = split[0]
        self.fixed_val = int(split[1])
        self.range_char = split[3]
        self.range_min = int(split[4])
        self.range_max = int(split[6])

    def get_x_max(self):
        if self.fixed_char == 'x':
            return self.fixed_val
        else:
            return self.range_max

    def get_y_max(self):
        if self.fixed_char == 'y':
            return self.fixed_val
        else:
            return self.range_max

    def get_x_min(self):
        if self.fixed_char == 'x':
            return self.fixed_val
        else:
            return self.range_min

    def get_y_min(self):
        if self.fixed_char == 'y':
            return self.fixed_val
        else:
            return self.range_min

    def draw(self, grid):
        if self.fixed_char == 'y':
            y = self.fixed_val
            for x in range(self.range_min, self.range_max+1):
                grid[y][x] = '#'
        elif self.fixed_char == 'x':
            x = self.fixed_val
            for y in range(self.range_min, self.range_max+1):
                grid[y][x] = '#'
        else:
            raise Exception("bad fixed_char")

def main():
    input_lines = get_input().splitlines()
    max_x = 0
    max_y = 0
    min_x = 9999
    min_y = 9999
    lines = []
    for l in input_lines:
        line = Line(l)
        max_x = max(max_x, line.get_x_max())
        max_y = max(max_y, line.get_y_max())
        min_x = min(min_x, line.get_x_min())
        min_y = min(min_y, line.get_y_min())
        lines.append(line)

    row = ['.'] * (max_x + 3)
    grid = []
    for y in range(max_y + 3):
        grid.append(list(row))

    for line in lines:
        line.draw(grid)

    spout = 500, 0
    run_down(grid, *spout, max_y)
    grid[spout[1]][spout[0]] = '+'

    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] in ['|','~']:
                total += 1

    # remove the blocks above min y from total
    total -= (min_y-1)

    return total


def run_down(grid, x, y, max_y):
    while y <= max_y:
        if grid[y][x] == '#':
            # hit floor
            fall_left, fall_right = None, None
            seen_drip_l, seen_drip_r = False, False # don't want to repeat recursion if already seen
            while not ((fall_left or seen_drip_l) or (fall_right or seen_drip_r)):
                y -= 1
                fall_left, fall_right, seen_drip_l, seen_drip_r = run_floor(grid, x, y)
            if fall_left and not seen_drip_l:
                run_down(grid, *fall_left, max_y)
            if fall_right and not seen_drip_r:
                run_down(grid, *fall_right, max_y)
            return

        else:
            # drip down
            grid[y][x] = '|'
            y += 1

def set_floor(grid, y, x_min, x_max):
    for x in range(x_min, x_max+1):
        grid[y][x] = '~'

def run_floor(grid, x, y):
    grid[y][x] = '~'
    # run left
    x_left = x-1
    fall_left = None
    seen_drip_l = False
    while True:
        if grid[y][x_left] == '#':
            # hit left barrier
            break
        elif grid[y+1][x_left] == '|':
            # hit fall we've already seen before
            seen_drip_l = True
            break
        elif grid[y+1][x_left] == '.':
            fall_left = (x_left, y)
            break
        x_left -= 1
    # run right
    x_right = x+1
    fall_right = None
    seen_drip_r = False
    while True:
        if grid[y][x_right] == '#':
            # hit right barrier
            break
        elif grid[y+1][x_right] == '|':
            # hit fall we've already seen before
            seen_drip_r = True
            break
        elif grid[y+1][x_right] == '.':
            fall_right = (x_right, y)
            break
        x_right += 1

    set_floor(grid, y, x_left+1, x_right-1)
    return fall_left, fall_right, seen_drip_l, seen_drip_r

if __name__ == "__main__":
    print(main())
