
input_file = "input.txt"

def get_input():
    return open(input_file, 'r').read()

def main():
    lines = get_input().splitlines()
    with_two = 0
    with_three = 0
    for line_idx, line1 in enumerate(lines):
        for line2 in lines[line_idx:]:
            num_diffs = 0
            diff_idx = None 
            for char_num in range(len(line1)):
                if line1[char_num] != line2[char_num]:
                    num_diffs += 1
                    diff_idx = char_num
            if num_diffs == 1:
                same = line1[:diff_idx] + line1[diff_idx+1:]
                return same

if __name__ == "__main__":
    print(main())
