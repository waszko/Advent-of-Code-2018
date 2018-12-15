
input_file = "input.txt"

def get_input():
    return open(input_file, 'r').read()

class Cart:
    def __init__(self, x, y, char, grid):
        self.x = x
        self.y = y
        self.dir = char
        self.grid = grid
        self.turn = 0 # next turn dir index: 0:L, 1:S, 2:R

    dir_map = {
        '/': {
            '<': 'v',
            '>': '^',
            '^': '>',
            'v': '<',
        },
        '\\': {
            '<': '^',
            '>': 'v',
            '^': '<',
            'v': '>',
        },
        '|': None,
        '-': None,
    }

    intersection_map = {
        '<': {
            0: 'v',
            1: '<',
            2: '^',
        },
        '>': {
            0: '^',
            1: '>',
            2: 'v',
        },
        '^': {
            0: '<',
            1: '^',
            2: '>',
        },
        'v': {
            0: '>',
            1: 'v',
            2: '<',
        }
    }

    def move(self):
        move_map = {
            '<' : (-1, 0),
            '>' : (1, 0),
            '^' : (0, -1),
            'v' : (0, 1),
        }
        movement = move_map[self.dir]
        self.x += movement[0]
        self.y += movement[1]

        # change direction
        grid_char = self.grid[self.y][self.x]
        if grid_char == '+':
            self.dir = self.intersection_map[self.dir][self.turn]
            self.turn = (self.turn + 1) % 3
        else:
            dir_change = self.dir_map[grid_char]
            if dir_change is not None:
                self.dir = dir_change[self.dir]

def main():
    inp = get_input().splitlines()
    inp = [list(line) for line in inp]
    y_size = len(inp)
    x_size = len(inp[0])
    carts = []

    # create cart objects and remove them from tracks
    for y in range(y_size):
        for x in range(x_size):
            if inp[y][x] in ['^', 'v', '<', '>']:
                carts.append(Cart(x, y, inp[y][x], inp))
                if inp[y][x] in ['<', '>']:
                    inp[y][x] = '-'
                else:
                    inp[y][x] = '|'

    def cart_sort(cart):
        return (cart.y * 1000) + cart.x

    steps = 0
    while len(carts) > 1:
        # sort carts by y
        carts.sort(key=cart_sort)

        # move and check for crash
        positions = {(cart.x, cart.y) : cart for cart in carts}
        carts_to_remove = set()
        for cart in carts:
            if cart in carts_to_remove:
                continue
            del positions[(cart.x, cart.y)]
            cart.move()
            if (cart.x, cart.y) in positions.keys():
                # crash
                carts_to_remove.add(cart)
                carts_to_remove.add(positions[(cart.x, cart.y)])
                del positions[cart.x, cart.y]
            else:
                positions[(cart.x, cart.y)] = cart

        # remove crashed carts
        if carts_to_remove:
            carts = [c for c in carts if c not in carts_to_remove]

    remaining = carts[0]
    return (remaining.x, remaining.y)


if __name__ == "__main__":
    print(main())
