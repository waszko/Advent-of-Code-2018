
input_file = "input.txt"

def get_input():
    return open(input_file, 'r').read()

class Point():
    def __init__(self, idx, line):
        split = line.split(', ')
        self.id = idx
        self.x = int(split[0])
        self.y = int(split[1])
        self.count = 0
        self.infinite = False

def main():
    lines = get_input().splitlines()
    points = [Point(i, l) for i, l in enumerate(lines)]
    max_x = -1
    max_y = -1
    min_x = 999
    min_y = 999
    for p in points:
        max_x = max(max_x, p.x)
        max_y = max(max_y, p.y)
        min_x = min(min_x, p.x)
        min_y = min(min_y, p.y)

    extend = 100
    max_x += extend
    max_y += extend
    min_x -= extend
    min_y -= extend
    for p in points:
        if p.x in [min_x, max_x] or p.y in [min_y, max_y]:
            print("inf")
            print((p.x, p.y))
            p.infinite = True

    def cmp_1(pair):
        return pair[1]

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            dists = [(p.id, abs(p.x - x) + abs(p.y - y)) for p in points]
            dists.sort(key=cmp_1)
            if dists[0][1] != dists[1][1]:
                min_dist = dists[0]
                min_p_id = min_dist[0]
                points[min_p_id].count += 1
                if x in [min_x, max_x] or y in [min_y, max_y]:
                    points[min_p_id].infinite = True

    non_inf = [p for p in points if not p.infinite]
    counts = [p.count for p in non_inf]
    counts.sort()
    return counts[-1]

if __name__ == "__main__":
    print(main())
