import re

input_file = "input.txt"

def get_input():
    return open(input_file, 'r').read()

class Star():
    def __init__(self, line):
        line = line.replace(' ', '')
        split = re.split('<|>|,', line)
        self.pos_x = int(split[1])
        self.pos_y = int(split[2])
        self.vel_x = int(split[4])
        self.vel_y = int(split[5])

def get_mins(stars):
    max_x = max([s.pos_x for s in stars])
    min_x = min([s.pos_x for s in stars])
    max_y = max([s.pos_y for s in stars])
    min_y = min([s.pos_y for s in stars])
    return (max_x - min_x) + (max_y - min_y)

def main():
    lines = get_input().splitlines()
    stars = [Star(line) for line in lines]

    prev_mins = 999999
    mins = get_mins(stars)
    while mins < prev_mins:
        prev_mins = mins
        for star in stars:
            star.pos_x += star.vel_x
            star.pos_y += star.vel_y
        mins = get_mins(stars)

    # undo last step
    for star in stars:
        star.pos_x -= star.vel_x
        star.pos_y -= star.vel_y

    star_set = set((s.pos_x, s.pos_y) for s in stars)

    min_x = min([s.pos_x for s in stars])
    min_y = min([s.pos_y for s in stars])
    max_x = max([s.pos_x for s in stars])
    max_y = max([s.pos_y for s in stars])
    answ = []
    for y in range(min_y, max_y + 1):
        line = []
        for x in range(min_x, max_x + 1):
            if (x,y) in star_set:
                line.append('x')
            else:
                line.append('.')
        answ.append(''.join(line))

    return '\n'.join(answ)

if __name__ == "__main__":
    print(main())
