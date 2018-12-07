
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
    node_costs = {n: ord(n)-64+60 for n in nodes}
    node_costs[None] = -1


    in_progress = set()
    done = []
    def get_next():
        ready = nodes.difference(set(done))
        for dep in deps:
            if dep[1] in ready:
                ready.remove(dep[1])
        ready = ready.difference(in_progress)
        if ready:
            ready_l = list(ready)
            ready_l.sort()
            next_node = ready_l[0]
        else:
            next_node = None
        return next_node

    def remove_finished(node):
        done.append(node)
        new_deps = set(d for d in deps if d[0] != node)
        return new_deps

    elves = [None] * 4
    count = 0

    while len(done) < len(nodes):
        for i in range(len(elves)):
            if elves[i] == None:
                elves[i] = get_next()
                in_progress.add(elves[i])

            node_costs[elves[i]] -= 1

        print(elves)
        for i in range(len(elves)):
            if node_costs[elves[i]] == 0:
                deps = remove_finished(elves[i])
                in_progress.remove(elves[i])
                elves[i] = None
 
        if len(done) < len(nodes):
            count += 1

    return count


if __name__ == "__main__":
    print(main())
