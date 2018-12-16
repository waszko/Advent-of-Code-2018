
input_file = "input.txt"

def get_input():
    return open(input_file, 'r').read()

def get_opcodes(regs):
    # Addition:
    def addr(a, b, c, r): # stores into register C the result of adding register A and register B.
        r[c] = r[a] + r[b]
    def addi(a, b, c, r): # stores into register C the result of adding register A and value B.
        r[c] = r[a] + b

    # Multiplication:
    def mulr(a, b, c, r): # stores into register C the result of multiplying register A and register B.
        r[c] = r[a] * r[b]
    def muli(a, b, c, r): # stores into register C the result of multiplying register A and value B.
        r[c] = r[a] * b

    # Bitwise AND:
    def banr(a, b, c, r): # stores into register C the result of the bitwise AND of register A and register B.
        r[c] = r[a] & r[b] 
    def bani(a, b, c, r): # stores into register C the result of the bitwise AND of register A and value B.
        r[c] = r[a] & b

    # Bitwise OR:
    def borr(a, b, c, r): # stores into register C the result of the bitwise OR of register A and register B.
        r[c] = r[a] | r[b]
    def bori(a, b, c, r): # stores into register C the result of the bitwise OR of register A and value B.
        r[c] = r[a] | b 

    # Assignment:
    def setr(a, b, c, r): # copies the contents of register A into register C. (Input B is ignored.)
        r[c] = r[a]
    def seti(a, b, c, r): # stores value A into register C. (Input B is ignored.)
        r[c] = a

    # Greater-than testing:
    def gtir(a, b, c, r): # sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
        r[c] = 1 if a > r[b] else 0
    def gtri(a, b, c, r): # sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
        r[c] = 1 if r[a] > b else 0
    def gtrr(a, b, c, r): # sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
        r[c] = 1 if r[a] > r[b] else 0

    # Equality testing:
    def eqir(a, b, c, r): # sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
        r[c] = 1 if a == r[b] else 0
    def eqri(a, b, c, r): # sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
        r[c] = 1 if r[a] == b else 0
    def eqrr(a, b, c, r): # sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
        r[c] = 1 if r[a] == r[b] else 0

    return set([addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr])


def main():
    regs = [0, 0, 0, 0]
    opcodes = get_opcodes(regs)

    # gather samples
    lines = get_input().splitlines()
    samples = []
    i = 0;
    while lines[i].startswith("Before"):
        before = list(map(int, lines[i][9:-1].split(', ')))
        instr  = list(map(int, lines[i+1].split(' ')))
        after  = list(map(int, lines[i+2][9:-1].split(', '))) 
        samples.append((before, instr, after))
        i += 4

    answ = 0
    for sample in samples:
        before, instr, after = sample

        count = 0
        for opcode in opcodes:
            regs = list(before)
            opcode(*instr[1:], regs)
            if regs == after:
                count += 1
        if count >= 3:
            answ += 1

    return answ 

if __name__ == "__main__":
    print(main())
