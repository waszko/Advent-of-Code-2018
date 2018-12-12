
input_file = "input.txt"

def get_input():
    return open(input_file, 'r').read()

def char_to_int(c):
    if c == "#":
        return 1
    if c == ".":
        return 0
    raise Exeption("bad char")

def get_state(line):
    return [char_to_int(c) for c in line[15:]]

def get_rule(line):
    inp = [char_to_int(c) for c in line[:5]]
    out = char_to_int(line[-1])
    return (tuple(inp), out)

def main():
    lines = get_input().splitlines()
    state = get_state(lines[0])
    rules = {get_rule(r)[0] : get_rule(r)[1] for r in lines[2:]}

    generations = 20
    extension = generations * 2 + 10
    state = ([0]*extension) + state + ([0]*extension)
    size = len(state)

    for gen in range(generations):
        new_state = [0] * size
        for i in range(2, size - 2):
            tup = tuple(state[i-2 : i+3])
            new_state[i] = rules[tup]
        state = new_state

    answ = 0
    for i in range(size):
        if state[i] == 1:
            answ += i - extension

    return answ
            
if __name__ == "__main__":
    print(main())
