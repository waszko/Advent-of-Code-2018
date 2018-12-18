from copy import deepcopy

input_file = "input.txt"

def get_input():
    return open(input_file, 'r').read()

def print_grid(grid):
    for line in grid:
        print(''.join(line))
    print()

def main():
    answer = 0
    lines = get_input().splitlines()
    grid = [list(line) for line in lines]
    y_size = len(grid)
    x_size = len(grid[0])

    for step in range(10):
        new_grid = deepcopy(grid)
        for y in range(y_size):
            for x in range(x_size):
                ground, trees, lumber = 0, 0, 0
                for y_adj in range(y-1, y+2):
                    for x_adj in range(x-1, x+2):
                        if ((x_adj == x and y_adj == y) or x_adj < 0 or y_adj < 0 or
                            x_adj >= x_size or y_adj >= y_size):
                            continue
                        adj_char = grid[y_adj][x_adj]
                        if adj_char == '.':
                            ground += 1
                        elif adj_char == '|':
                            trees += 1
                        elif adj_char == '#':
                            lumber += 1
                        else:
                            raise Exception("bad char")
                prev_char = grid[y][x]
                if prev_char == '.':
                    if trees >= 3:
                        new_grid[y][x] = '|'
                elif prev_char == '|':
                    if lumber >= 3:
                        new_grid[y][x] = '#'
                elif prev_char == '#':
                    if not (lumber >= 1 and trees >= 1):
                        new_grid[y][x] = '.'
        grid = new_grid

    trees = 0
    lumber = 0
    for y in range(y_size):
        for x in range(x_size):
            char = grid[y][x]
            if char == '|':
                trees += 1
            elif char == '#':
                lumber += 1

    return trees * lumber

if __name__ == "__main__":
    print(main())
