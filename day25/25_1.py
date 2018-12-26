
input_file = "input.txt"

def get_input():
    return open(input_file, 'r').read()

def manhattan(a, b):
    return (abs(a[0] - b[0]) + 
            abs(a[1] - b[1]) + 
            abs(a[2] - b[2]) + 
            abs(a[3] - b[3]))

def main():
    lines = get_input().splitlines()
    points = []
    for line in lines:
        points.append(tuple(map(int, line.split(','))))
    limit = 3

    constelations = []
    for point in points:
        in_consts = [] # list of consts this point is in
        for const in constelations:
            for const_point in const:
                dist = manhattan(point, const_point)
                if dist <= limit:
                    in_consts.append(const)
                    break # no need to check more points
        if in_consts:
            # add point to union of consts it is in
            joined_const = set([point])
            for const in in_consts:
                joined_const = joined_const.union(const)
                constelations.remove(const)
            constelations.append(joined_const)
        else:
            # point hasn't been added to any constelation, make a new one
            const = set([point])
            constelations.append(const)

    return len(constelations)

if __name__ == "__main__":
    print(main())
