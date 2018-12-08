
input_file = "input.txt"

def get_input():
    return open(input_file, 'r').read()

def main():
    line = get_input().splitlines()[0]
    nums = list(map(int, line.split(' ')))

    i = 0
    def process():
        nonlocal i
        children_count = nums[i]
        metadata_count = nums[i+1]
        i += 2
        children = [process() for c in range(children_count)]
        metadata = [nums[i+m] for m in range(metadata_count)]
        i += metadata_count

        value = 0
        if children_count == 0:
            value = sum(metadata)
        else:
            for m in metadata:
                if m > 0 and m <= children_count:
                    value += children[m-1]

        return value

    root_val = process()
    return root_val

if __name__ == "__main__":
    print(main())
