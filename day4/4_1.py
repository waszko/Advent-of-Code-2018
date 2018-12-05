
input_file = "input.txt"

def get_input():
    return open(input_file, 'r').read()

def compare_dates_key(line):
    # [1518-09-06 00:47] ... -> 09060047
    return int(line[6:8] + line[9:11] + line[12:14] + line[15:17])

class Guard:
    def __init__(self, id_num):
        self.id = id_num
        self.sleep = []
        self.sleep_total = 0

    def add_day(self):
        day = [0] * 60
        self.sleep.append(day)

    def add_sleep(self, sleep_time, wake_time):
        for i in range(sleep_time, wake_time):
            self.sleep[-1][i] = 1
        self.sleep_total += wake_time - sleep_time


def main():
    lines = get_input().splitlines()
    lines.sort(key=compare_dates_key)
    guards = {}
    i = 0
    while i < len(lines):
        guard_line = lines[i]
        id_num = int(guard_line.split()[3][1:])
        if id_num not in guards:
            guards[id_num] = Guard(id_num)
        guard = guards[id_num]
        guard.add_day()
        i += 1
        while i < len(lines) and lines[i].split()[2] != 'Guard':
            sleep_time = int(lines[i][15:17])
            wake_time  = int(lines[i+1][15:17])
            guard.add_sleep(sleep_time, wake_time)
            i += 2

    max_sleep_guard = (None, -1)
    for guard in guards.values():
        if guard.sleep_total > max_sleep_guard[1]:
            max_sleep_guard = (guard, guard.sleep_total)

    sleep_by_min = [0] * 60
    sleep = max_sleep_guard[0].sleep
    for day in sleep:
        for i in range(60):
            sleep_by_min[i] += day[i]
    max_idx = sleep_by_min.index(max(sleep_by_min))

    return max_sleep_guard[0].id * max_idx

if __name__ == "__main__":
    print(main())
