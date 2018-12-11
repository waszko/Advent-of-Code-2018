
def main():
    serial_num = 5093
    size = 300
    grid = []
    for y in range(1, size + 1):
        row = []
        for x in range(1, size + 1):
            rack_id = x + 10
            power_lvl = rack_id * y
            power_lvl += serial_num
            power_lvl *= rack_id
            power_lvl = (power_lvl // 100) % 10
            power_lvl -= 5
            row.append(power_lvl)
        grid.append(row)

    grid_t = list(map(list, zip(*grid))) # transpose

    max_coords = None
    max_val = -999
    sum_size = 3
    calced = {}
    for sum_size in range(1, size + 1):
        # print(sum_size)
        for y in range(0, size - sum_size):
            # compute columns to speed up below
            columns = [sum(grid_t[x][y:y+sum_size]) for x in range(size)]
            for x in range(0, size - sum_size):
                if x == 0:
                    if y == 0:
                        # compute whole sub grid
                        val = 0
                        for ys in range(sum_size):
                            for xs in range(sum_size):
                                val += grid[y + ys][x + xs]
                    else:
                        # compute first in row from prev_row_val
                        val = prev_row_val
                        for xs in range(sum_size):
                            val -= grid[y-1][x+xs] 
                            val += grid[y+sum_size-1][x+xs]
                    prev_row_val = val
                else:
                    # compute next in row
                    val = prev_val
                    val -= columns[x-1]
                    val += columns[x+sum_size-1]

                prev_val = val

                if val > max_val:
                    max_val = val
                    max_coords = (x+1, y+1, sum_size)

    return max_coords

if __name__ == "__main__":
    print(main())
