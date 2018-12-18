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

    seen = []
    prev_score0 = None
    prev_score1 = None
    seq_idxs = set()
    stop = False
    step = 0
    while not stop:
        step += 1
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
        score = get_score(grid, x_size, y_size)
        if score in seen:
            idx = seen.index(score)
            if seen[idx-1] == prev_score0 and seen[idx-2] == prev_score1:
                if idx in seq_idxs:
                    stop = True
                else:
                    seq_idxs.add(idx)
                    seq_idxs.add(idx-1)
                    seq_idxs.add(idx-2)
        seen.append(score)
        prev_score1 = prev_score0
        prev_score0 = score

    idx = 1000000000
    idx -= min(seq_idxs)
    idx = (idx-1) % len(seq_idxs)
    return seen[min(seq_idxs) + idx]

def get_score(grid, x_size, y_size):
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
