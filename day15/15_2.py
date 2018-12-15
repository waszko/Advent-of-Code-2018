from copy import deepcopy
from dataclasses import dataclass

input_file = "input.txt"

def get_input():
    return open(input_file, 'r').read()

@dataclass(unsafe_hash=True)
class Creature:
    type: str
    x: int
    y: int
    hp: int = 200
    attack: int = 3

def creature_sort(c):
    return (1000 * c.y) + c.x

def main():
    cave = get_input().splitlines()
    cave = [list(line) for line in cave]
    y_size = len(cave)
    x_size = len(cave[0])

    creatures = []
    for y in range(y_size):
        for x in range(x_size):
            if cave[y][x] in ['G', 'E']: 
                creatures.append(Creature(type=cave[y][x], x=x, y=y))

    elf_attack = 4
    survived = False
    while not survived:
        # print("attack = " + str(elf_attack))
        (survived, result) = run(deepcopy(cave), deepcopy(creatures), elf_attack)
        elf_attack += 1
    return result

# retuns (bool: elves survived, int: result if they did)
def run(cave, creatures, elf_attack):
    for c in creatures:
        if c.type == 'E':
            c.attack = elf_attack

    turn = 0
    while True:
        creatures.sort(key=creature_sort)
        died = set()
        for cret in creatures:
            if cret.hp <= 0:
                continue
            enemies = [c for c in creatures if c.type != cret.type and c.hp > 0]

            adjacents = get_adjacent_spots(cave, cret, enemies)

            # find shortest path to an adjacent (BFS)
            shortest_path = bfs(cave, (cret.x, cret.y), adjacents)
            if not shortest_path:
                continue # none reachable

            if len(shortest_path) > 1:
                pos = shortest_path[1]
                move(cave, cret, pos)

            targets = get_targets(cret, enemies)
            if targets:
                targets.sort(key=target_sort)
                target = targets[0]

                elf_died = attack(cret, target, cave, died)
                if elf_died:
                    return False, -1


            types_left = set(c.type for c in creatures if c.hp > 0)
            if len(types_left) < 2:
                hp_total = sum([c.hp for c in creatures if c.hp > 0])
                return True, turn * hp_total

        creatures = [c for c in creatures if c not in died]
        # print(creatures)
        # print_cave(cave)
        turn += 1

def get_adjacent_spots(cave, cret, enemies):
    adjacents = []
    for enemy in enemies:
        for adj in [(1,0), (-1,0), (0,1), (0,-1)]:
            x = enemy.x + adj[0]
            y = enemy.y + adj[1]
            if cave[y][x] == '.' or (x,y) == (cret.x, cret.y):
                adjacents.append((x,y)) 
    return adjacents


def bfs(cave, start, ends):
    queue = [[start]]
    seen = set()
    while queue:
        path = queue.pop(0)
        curr = path[-1]
        if curr in ends:
            return path
        elif curr not in seen:
            possible_moves = [(0,-1), (-1,0), (1,0), (0,1)] # read order
            for move in possible_moves:
                x = curr[0] + move[0]
                y = curr[1] + move[1]
                if cave[y][x] == '.':
                    new_path = list(path)
                    new_path.append((x,y))
                    queue.append(new_path)
            seen.add(curr)

def move(cave, cret, pos):
    cave[cret.y][cret.x] = '.'
    (cret.x, cret.y) = pos
    cave[cret.y][cret.x] = cret.type

def get_targets(cret, enemies):
    targets = []
    for adj in [(1,0), (-1,0), (0,1), (0,-1)]:
        x = cret.x + adj[0]
        y = cret.y + adj[1]
        for enemy in enemies:
            if (x,y) == (enemy.x, enemy.y):
                targets.append(enemy)
    return targets

def target_sort(t):
    return (t.hp * 1000 * 1000) + (t.y * 1000) + t.x

# returns bool elf_died
def attack(cret, target, cave, died):
    target.hp -= cret.attack
    if target.hp <= 0: # killed
        cave[target.y][target.x] = '.'
        died.add(target)
        if target.type == 'E':
            return True
    return False


def print_cave(cave):
    print()
    for line in cave:
        print (''.join(line))
    print()

if __name__ == "__main__":
    print(main())
