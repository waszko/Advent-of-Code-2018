import re

input_file = "input.txt"

def get_input():
    return open(input_file, 'r').read()

class Group:
    def __init__(self, id_, army, line):
        self.name = army + " " + str(id_)
        split = re.split(' |\(|\)|,|;', line)
        self.units = int(split[0])
        self.hp = int(split[4])
        if 'weak' in line:
            weak_idx = line.index('weak')
            end_idx = line.find(';', weak_idx)
            if end_idx == -1:
                end_idx = line.find(')', weak_idx)
            weak_str = line[weak_idx+8 : end_idx]
            self.weaks = weak_str.split(', ')
        else:
            self.weaks = []
        if 'immune' in line:
            immune_idx = line.index('immune')
            end_idx = line.find(';', immune_idx)
            if end_idx == -1:
                end_idx = line.find(')', immune_idx)
            immune_str = line[immune_idx+10 : end_idx]
            self.immunes = immune_str.split(', ')
        else:
            self.immunes = []
        attack_idx = split.index('attack') 
        self.damage = int(split[attack_idx+3])
        self.attack = split[attack_idx+4]
        self.init = int(split[attack_idx+8])

        # used during battle
        self.targeted = False
        self.target = None

    def effective_power(self):
        return self.units * self.damage

    def attacked(self, attacker):
        dmg = get_damage(attacker=attacker, defender=self)
        killed = min(dmg // self.hp, self.units)
        self.units -= killed


def cmp_group_ep(group):
    return (-1 * group.effective_power() * 1000) + (-1 * group.init)

def cmp_group_init(group):
    return -1 * group.init

def get_damage(attacker, defender):
    if attacker.attack in defender.immunes:
        return 0
    dmg = attacker.effective_power()
    if attacker.attack in defender.weaks:
        dmg *= 2
    return dmg


class Army:
    def __init__(self, name):
        self.name = name
        self.groups = set()

    def __repr__(self):
        rtn = "\n"
        for group in self.groups:
            rtn += str(group.name) + " " + str(group.units) + " units\n"
        return rtn


def main():
    # parse armies
    lines = get_input().splitlines()
    i = 0
    armies = []
    while i < len(lines):
        line = lines[i]
        army_name = line[:-1]
        army = Army(army_name)
        group_count = 1
        i += 1
        while i < len(lines) and lines[i]:
            line = lines[i]
            army.groups.add(Group(group_count, army_name, line))
            group_count += 1
            i += 1
        armies.append(army)
        i += 1

    all_groups = list(armies[0].groups.union(armies[1].groups))

    # run battle
    while armies[0].groups and armies[1].groups:

        # target selection phase
        all_groups.sort(key=cmp_group_ep)
        for group in all_groups:
            enemy_army = armies[0] if group in armies[1].groups else armies[1]
            enemies = [g for g in enemy_army.groups if not g.targeted]
            if enemies:
                def cmp_attack(enemy):
                    dmg = get_damage(attacker=group, defender=enemy)
                    return (dmg * 1000  * 1000) + (enemy.effective_power() * 1000) + enemy.init
            
                target = max(enemies, key=cmp_attack)
                if get_damage(attacker=group, defender=target) == 0:
                    # cant deal damage to anyone, attack no one
                    group.target = None
                else:
                    group.target = target
                    target.targeted = True
            else:
                # no untargetted enemies remain
                group.target = None

        # attack phase
        all_groups.sort(key=cmp_group_init)
        for group in all_groups:
            target = group.target
            if target:
                target.attacked(group)
                if target.units == 0:
                    all_groups.remove(target)
                    if target in armies[0].groups:
                        armies[0].groups.remove(target)
                    else:
                        armies[1].groups.remove(target)

        # reset things for next target selection phase
        for group in all_groups:
            group.target = None
            group.targeted = False

    # only one army remaining at this point
    sum_units = 0
    for group in all_groups:
        sum_units += group.units

    return sum_units
    

if __name__ == "__main__":
    print(main())
