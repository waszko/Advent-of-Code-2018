
input_file = "input.txt"

def get_input():
    return open(input_file, 'r').read()

def main():
    line = get_input().splitlines()[0]
    nums = list(map(int, line.split(' ')))

    i = 0
    meta_sum = 0
    def process():
        nonlocal i, meta_sum
        children = nums[i]
        metadata = nums[i+1]
        i += 2
        for c in range(children):
            process()
        for m in range(metadata):
            meta_sum += nums[i]
            i += 1

    process()
    return meta_sum

if __name__ == "__main__":
    print(main())
