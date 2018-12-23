from dataclasses import dataclass
import re

input_file = "input.txt"

def get_input():
    return open(input_file, 'r').read()

@dataclass(unsafe_hash=True)
class Bot:
    x: int
    y: int
    z: int
    r: int

def cmp_range(bot):
    return bot.r 

def main():
    lines = get_input().splitlines()
    bots = set()
    for line in lines:
        s = re.split('<|>|,|=', line)
        bot = Bot(x=int(s[2]), y=int(s[3]), z=int(s[4]), r=int(s[7]))
        bots.add(bot)

    max_bot = max(bots, key=cmp_range)

    in_range = 0
    for bot in bots:
        x_dist = abs(bot.x - max_bot.x)
        y_dist = abs(bot.y - max_bot.y)
        z_dist = abs(bot.z - max_bot.z)
        dist = x_dist + y_dist + z_dist
        if dist <= max_bot.r:
            in_range += 1

    return in_range

if __name__ == "__main__":
    print(main())
