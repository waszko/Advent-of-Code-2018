
input_file = "input.txt"

def get_input():
    return open(input_file, 'r').read()

def main():
    poly_orig = get_input().strip()
    chars = set(poly_orig.lower())
    lens = []
    for c in chars:
        poly = poly_orig.replace(c.lower(), "").replace(c.upper(), "")
        i = 0
        while i < len(poly)-1:
            if ((poly[i].lower() == poly[i+1].lower()) and 
                ((poly[i].isupper() and poly[i+1].islower()) or
                 (poly[i].islower() and poly[i+1].isupper()))):
                poly = poly[:i] + poly[i+2:]
                i = max(i-1, 0)
            else:
                i += 1
        lens.append(len(poly))
    return min(lens)


if __name__ == "__main__":
    print(main())
