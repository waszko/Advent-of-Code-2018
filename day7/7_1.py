
input_file = "input.txt"

def get_input():
    return open(input_file, 'r').read()

def main():
    deps = set()
    lines = get_input().splitlines()
    for line in lines:
        split = line.split()
        deps.add((split[1], split[7]))

    nodes = set(d[0] for d in deps)
    nodes = nodes.union(set(d[1] for d in deps))

    order = []
    while len(order) < len(nodes):
        ready = nodes.difference(set(order))
        for dep in deps:
            if dep[1] in ready:
                ready.remove(dep[1])
        ready_l = list(ready)
        ready_l.sort()
        next_node = ready_l[0]
        order.append(next_node)
        new_deps = set(d for d in deps if d[0] != next_node)
        deps = new_deps
    return ''.join(order)



if __name__ == "__main__":
    print(main())
