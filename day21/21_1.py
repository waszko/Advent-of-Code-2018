
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

    return {
        'addr': addr,
        'addi': addi,
        'mulr': mulr,
        'muli': muli,
        'banr': banr,
        'bani': bani,
        'borr': borr,
        'bori': bori,
        'setr': setr,
        'seti': seti,
        'gtir': gtir,
        'gtri': gtri,
        'gtrr': gtrr,
        'eqir': eqir,
        'eqri': eqri,
        'eqrr': eqrr
    }


def main():
    opcodes = get_opcodes()

    lines = get_input().splitlines()
    ip_reg = int(lines[0].split()[1])
    lines = lines[1:]

    regs = [0,0,0,0,0,0]

    ip = 0
    while ip < len(lines):
        regs[ip_reg] = ip
        line = lines[ip]
        split = line.split()
        opcode = opcodes[split[0]]
        args = map(int, split[1:])
        opcode(*args, regs)

        ip = regs[ip_reg]
        ip += 1
        if ip == 28:
            return regs[5]

    return regs[0]

if __name__ == "__main__":
    print(main())

# 0, 1, 2, 3, 4,     5 
#[0, 1, 0, 0, 0, 13431073]

#ip 1
# seti 123 0 5      : r5 = 123
# bani 5 456 5      : r5 &= 456
# eqri 5 72 5       : r5 = 1 if r5 == 72 else 0
# addr 5 1 1        : r1 += r5 
# seti 0 0 1        : r1 = 0
# seti 0 6 5        : r5 = 0
# bori 5 65536 4    : r4 = r5 || 65536
# seti 13431073 4 5 : r5 = 13431073
# bani 4 255 3      : r3 = r4 && 255
# addr 5 3 5        : r5 += r3
# bani 5 16777215 5 : r5 &= 16777215
# muli 5 65899 5    : r5 *= 65899
# bani 5 16777215 5 : r5 &= 16777215
# gtir 256 4 3      : r3 = 1 if 256 > r4 else 0
# addr 3 1 1        : r1 += r3
# addi 1 1 1        : r1 += 1
# seti 27 9 1       : r1 = 27
# seti 0 1 3        : r3 = 0
# addi 3 1 2        : r2 = r3 + 1
# muli 2 256 2      : r2 *= 256
# gtrr 2 4 2        : r2 = 1 if r2 > r4 else 0
# addr 2 1 1        : r1 += r2
# addi 1 1 1        : r1 += 1
# seti 25 4 1       : r1 = 25
# addi 3 1 3        : r3 += 1
# seti 17 8 1       : r1 = 17
# setr 3 4 4        : r4 += r3
# seti 7 7 1        : r1 = 7
# eqrr 5 0 3        : r3 = 1 if r5 == r0 else 0
# addr 3 1 1        : r1 += r3
# seti 5 9 1        : r1 = 5

