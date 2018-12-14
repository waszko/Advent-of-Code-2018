
def main():
    num = "864801"
    num = [int(n) for n in num]
    num_len = len(num)
    recipes = [3, 7]
    size = len(recipes)
    elf1 = 0
    elf2 = 1

    while recipes[size-num_len:] != num and recipes[size-num_len-1:-1] != num:
        sum_ = recipes[elf1] + recipes[elf2]
        for char in str(sum_):
            recipes.append(int(char))
        size = len(recipes)
        elf1 = (elf1 + recipes[elf1] + 1) % size
        elf2 = (elf2 + recipes[elf2] + 1) % size

    if recipes[size-num_len:] == num:
        return size - num_len
    else: # recipes[size-num_len-1:-1] == num
        return size - num_len - 1




if __name__ == "__main__":
    print(main())
