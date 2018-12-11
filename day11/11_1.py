
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

    max_coords = None
    max_val = -999
    for y in range(size - 3):
        for x in range(size - 3):
            val = 0
            for ys in range(3):
                for xs in range(3):
                    val += grid[y + ys][x + xs]
            if val > max_val:
                max_val = val
                max_coords = (x+1, y+1)

    return max_coords

if __name__ == "__main__":
    print(main())
