
input_file = "input.txt"

class Rect:
    def __init__(self, line):
        split = line.split(' ')
        self.id = split[0][1:]
        self.x_min = int(split[2].split(',')[0])
        self.y_min = int(split[2].split(',')[1][:-1])
        self.width = int(split[3].split('x')[0])
        self.height = int(split[3].split('x')[1])
        self.x_max = self.x_min + self.width
        self.y_max = self.y_min + self.height

def get_input():
    return open(input_file, 'r').read()

def main():
    lines = get_input().splitlines()
    rects = [Rect(line) for line in lines]

    seen = {}
    dups = set()
    touching = set()
    for rect in rects:
        for x in range(rect.x_min, rect.x_max):
            for y in range(rect.y_min, rect.y_max):
                if (x,y) in seen.keys():
                    dups.add((x,y))
                    seen[(x,y)].append(rect.id)
                    for rect_id in seen[(x,y)]:
                        touching.add(rect_id)
                else:
                    seen[(x,y)] = [rect.id]

    for rect in rects:
        if rect.id not in touching:
            return rect.id

if __name__ == "__main__":
    print(main())
