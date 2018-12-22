def main():

    target = 10551378
    r1 = 0
    r5 = 1
    r0 = 0

    while r5<= target:
        # # r2 = 1 # 02
        # # while r2 <= target:
        # for i in range(1, target+1):
        #     if (r5 * i) == target:
        #         r0 += r5
        # #     r2 += 1
        if target % r5 == 0:
            r0 += r5
        r5 += 1

    return r0

if __name__ == "__main__":
    print(main())

#  0, 1, 2,         3!  4,         5
# [0, 0, 105504629, 12, 105504628, 105504629]
#     ^flag         ^pc

# #ip 3
# 00: addi 3 16 3. [3] += 16
# 01: seti 1 6 5   [5] = 1
# 02: seti 1 8 2   [2] = 1
# 03: mulr 5 2 1   [1] = [5]*[2]
# 04: eqrr 1 4 1   [1] =  1 if [1]==[4] else 0 <-- if true go to 7 else to 8
# 05: addr 1 3 3   [3] += [1]
# 06: addi 3 1 3   [3] += 1 <-- go to 8
# 07: addr 5 0 0   [0] += [5]
# 08: addi 2 1 2   [2] += 1
# 09: gtrr 2 4 1   [1] =  1 if [2]>[4] else 0 <-- if true go to 12 else loop back to 3
# 10: addr 3 1 3   [3] += [1]
# 11: seti 2 3 3   [3] = 2 <--- loop back to 3
# 12: addi 5 1 5   [5] += 1
# 13: gtrr 5 4 1   [1] = 1 if [5]>[4] else 0 <-- if true EXIT else to 2
# 14: addr 1 3 3   [3] += [1]
# 15: seti 1 8 3   [3] = 1
# 16: mulr 3 3 3   [3] = [3]^2
# 17: addi 4 2 4   [4] += 2
# 18: mulr 4 4 4   [4] = [4]^2
# 19: mulr 3 4 4   [4] *= [3]
# 20: muli 4 11 4  [4] *= 11
# 21: addi 1 6 1   [1] += 6
# 22: mulr 1 3 1   [1] *= [3]
# 23: addi 1 10 1  [1] += 10
# 24: addr 4 1 4   [4] += 1
# 25: addr 3 0 3   [3] += [0] <-- skips over 26 unless [0]==0
# 26: seti 0 0 3   [3] = 0
# 27: setr 3 9 1   [1] = [3]
# 28: mulr 1 3 1   [1] *= [3]
# 29: addr 3 1 1   [1] += [3]
# 30: mulr 3 1 1   [1] *= [3]
# 31: muli 1 14 1  [1] *= 14
# 32: mulr 1 3 1   [1] *= [3]
# 33: addr 4 1 4   [4] += [1] <-- after 1st iter [4] = 105504628
# 34: seti 0 4 0   [0] = 0
# 35: seti 0 0 3   [3] = 0
