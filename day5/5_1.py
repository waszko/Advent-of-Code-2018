
input_file = "input.txt"

def get_input():
    return open(input_file, 'r').read()

def main():
    poly = get_input().strip()
    i = 0
    while i < len(poly)-1:
        if ((poly[i].lower() == poly[i+1].lower()) and 
            ((poly[i].isupper() and poly[i+1].islower()) or
             (poly[i].islower() and poly[i+1].isupper()))):
            poly = poly[:i] + poly[i+2:]
            i -= 1
        else:
            i += 1
    return len(poly)


if __name__ == "__main__":
    print(main())
