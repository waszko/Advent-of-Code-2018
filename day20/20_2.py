from copy import deepcopy

input_file = "input.txt"

def get_input():
    return open(input_file, 'r').read()

move_map = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0)
}

def main():
    inp = get_input().splitlines()[0]
    inp = inp[1:-1]

    room_map = {
        (0,0): 0
    }

    coord = (0,0,0) # x, y, steps
    coords = [coord]
    run(inp, 0, coords, room_map)

    at_least_1000 = len([x for x in room_map.values() if x >= 1000])
    return at_least_1000

def run(inp, idx, coords, room_map):
    while idx < len(inp):
        char = inp[idx]
        if char == "(":
            # find ) index (idx2)
            split_idxs = [idx]
            end_idx = idx+1
            nest_level = 0
            while not (nest_level == 0 and inp[end_idx] == ')'):
                if inp[end_idx] == "(":
                    nest_level += 1
                elif inp[end_idx] == ")":
                    nest_level -= 1
                elif nest_level == 0 and inp[end_idx] == "|":
                    split_idxs.append(end_idx)
                end_idx +=1

            # recurse into each half
            new_coords = []
            for coord in coords:
                for split_idx in split_idxs:
                    new_coords += run(inp, split_idx+1, deepcopy(coords), room_map)
            coords = new_coords # todo temp commented out
            idx = end_idx+1    
        elif char == "|":
            # finished first half
            return coords
        elif char == ")":
            # finished 2nd half
            return coords
        else: # NESW
            movement = move_map[char]

            for i, coord in enumerate(coords):
                moved_coord = (coord[0]+movement[0], coord[1]+movement[1])
                steps = coord[2] + 1
                if moved_coord in room_map:
                    steps = min(room_map[moved_coord], steps)
                room_map[moved_coord] = steps
                coords[i] = (moved_coord[0], moved_coord[1], coord[2]+1)

            # TODO rejoin coords which match
            coords_map = {}
            for coord in coords:
                if (coord[0], coord[1]) in coords_map:
                    coords_map[(coord[0], coord[1])] = min(coords_map[(coord[0], coord[1])], coord[2])
                else:
                    coords_map[(coord[0], coord[1])] = coord[2]
            if len(coords_map.keys()) < len(coords):
                new_coords = []
                for coord, steps in coords_map.items():
                    new_coords.append((coord[0], coord[1], steps))
                coords = new_coords

            idx += 1

if __name__ == "__main__":
    print(main())
