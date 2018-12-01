
input_file = "input.txt"

def get_input():
    return open(input_file, 'r').read()

def main():
    freq = 0
    seen_freqs = set()
    lines = get_input().splitlines()
    i = 0
    while True:
        line = lines[i]
        seen_freqs.add(freq)
        num = int(line[1:])
        if line[0] == '+':
            freq += num
        elif line[0] == '-':
            freq -= num
        else:
            raise Exception()
        if freq in seen_freqs:
            return freq
        i = (i+1) % len(lines)

if __name__ == "__main__":
    print(main())
