
def main():
    num = 864801
    recipes = [3, 7]
    size  = len(recipes)
    elf1 = 0
    elf2 = 1

    while size < num + 10:
        sum_ = recipes[elf1] + recipes[elf2]
        for char in str(sum_):
            recipes.append(int(char))
        size = len(recipes)
        elf1 = (elf1 + recipes[elf1] + 1) % size
        elf2 = (elf2 + recipes[elf2] + 1) % size

    string = ''.join(str(n) for n in recipes[num:])
    return string

if __name__ == "__main__":
    print(main())
