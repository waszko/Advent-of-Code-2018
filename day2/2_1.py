
input_file = "input.txt"

def get_input():
    return open(input_file, 'r').read()

def main():
    lines = get_input().splitlines()
    with_two = 0
    with_three = 0
    for line in lines:
        chars = {}
        has_two = False
        has_three = False
        for char in line:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1

        for char, val in chars.items():
            if val == 2:
                has_two = True
            elif val == 3:
                has_three = True

        if has_two:
            with_two += 1
        if has_three:
            with_three += 1

    return with_two * with_three

if __name__ == "__main__":
    print(main())
