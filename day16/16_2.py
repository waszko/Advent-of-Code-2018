
input_file = "input.txt"

def get_input():
    return open(input_file, 'r').read()

def get_opcodes():
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

    return [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]


def main():
    opcodes = get_opcodes()

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

    poss_instr_map = {} # map from instr_num to idx of possible opcodes
    for sample in samples:
        before, instr, after = sample

        count = 0
        for opcode_num, opcode in enumerate(opcodes):
            regs = list(before)
            instr_num = instr[0]
            opcode(*instr[1:], regs)
            if regs == after:
                if instr_num in poss_instr_map:
                    poss_instr_map[instr_num].add(opcode_num)
                else:
                    poss_instr_map[instr_num] = set([opcode_num])


    instr_map = {} # final 1 to 1 map
    while len(instr_map) < len(poss_instr_map):
        for instr_num, poss_opcodes in poss_instr_map.items():
            if len(poss_opcodes) == 1:
                final_opcode = poss_opcodes.pop()
                instr_map[instr_num] = final_opcode
                # del poss_instr_map[instr_num]
                for other_poss_opcodes in poss_instr_map.values():
                    if final_opcode in other_poss_opcodes:
                        other_poss_opcodes.remove(final_opcode)

    # parse program
    program_start = i+2
    instrs = [] # list of pairs of (opcode, args)
    for line in lines[program_start:]:
        instr = list(map(int, line.split(' ')))
        opcode = opcodes[instr_map[instr[0]]]
        instrs.append((opcode, instr[1:]))

    # run program
    regs = [0,0,0,0]
    for opcode, args in instrs:
        opcode(*args, regs)

    return regs[0]

if __name__ == "__main__":
    print(main())
