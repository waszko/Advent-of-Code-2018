
input_file = "input.txt"

def get_input():
    return open(input_file, 'r').read()

def main():
    answer = 0
    lines = get_input().splitlines()
    for line in lines:
    	num = int(line[1:])
    	if line[0] == '+':
    		answer += num
    	elif line[0] == '-':
    		answer -= num
    	else:
    		raise Exception()
    return answer

if __name__ == "__main__":
    print(main())
