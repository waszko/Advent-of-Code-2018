from dataclasses import dataclass
import heapq
import random

input_file = "input.txt"

@dataclass()
class Point:
    x: int
    y: int

class Node:
    def __init__(self, x, y, tool):
        self.x = x
        self.y = y
        self.tool = tool
        self.edges = [] # list of (weight, node) pairs

        # for dykstras:
        self.visited = False
        self.distance = None
        self.id = random.random() # for breaking sorting ties


    def __repr__(self):
        rtn = "(" + str(self.x) + "," + str(self.y) + "," + self.tool + ")[" 
        for edge in self.edges:
            rtn += str(edge[0]) + ":(" + str(edge[1].x) + "," + str(edge[1].y) + "," + edge[1].tool + "),"
        rtn += "]"
        return rtn

def get_input():
    return open(input_file, 'r').read()

def main():
    lines = get_input().splitlines()
    depth = int(lines[0].split()[1])
    # depth = 510
    target = tuple(map(int, lines[1].split()[1].split(',')))
    # target = (10,10)
    target = Point(x=target[0], y=target[1])

    size_x = int(target.x * 15)
    size_y = int(target.y * 15)

    # define cave
    cave = []
    for y in range(size_y):
        cave.append([0] * (size_x))

    # set mouth val
    cave[0][0] = 0  

    # set y=0 vals
    for x in range(size_x):
        cave[0][x] = x * 16807

    # set x=0 vals
    for y in range(size_y):
        cave[y][0] = y * 48271

    # set rest of the vals
    for y in range(1, size_y):
        for x in range(1, size_x):
            erosion_x = (cave[y][x-1] + depth) % 20183
            erosion_y = (cave[y-1][x] + depth) % 20183
            cave[y][x] = erosion_x * erosion_y

    # get risk levels
    type_map = {
        0: '.', # rocky
        1: '=', # wet
        2: '|', # narrow
    }
    risk_level = 0
    for y in range(0, size_y):
        for x in range(0, size_x):
            if (x==0 and y==0) or (x==target.x and y==target.y):
                cave[y][x] = "X"
                continue
            erosion = (cave[y][x] + depth) % 20183
            risk_level += erosion % 3
            cave[y][x] = type_map[erosion%3]

    # generate nodes
    tool_map = {
        '.': ['c','t'],
        '=': ['c','n'],
        '|': ['t','n'],
        'X': [] # todo change this?
    }
    nodes = {} # map from (x,y) to list of nodes
    for y in range(0, size_y):
        for x in range(0, size_x):
            nodes[(x,y)] = []
            for tool in tool_map[cave[y][x]]:
                node = Node(x=x, y=y, tool=tool)
                nodes[(x,y)].append(node)
    # edges of cave are empty
    for x in range(-1, size_x):
        nodes[(x,-1)] = []
        nodes[(x,size_y)] = []
    for y in range(-1, size_y):
        nodes[(-1, y)] = []
        nodes[(size_x,y)] = []
    mouth = Node(x=0, y=0, tool='t')
    nodes[(0,0)] = [mouth]
    end = Node(x=target.x, y=target.y, tool='t')
    end_c = Node(x=target.x, y=target.y, tool='c')
    nodes[(target.x,target.y)] = [end, end_c]

    # link nodes
    for y in range(0, size_y):
        for x in range(0, size_x):
            neighbours = nodes[(x+1,y)] + nodes[(x-1,y)] + nodes[(x,y+1)] + nodes[(x,y-1)] 
            for node in nodes[(x,y)]:
                # add edges to neighbours with the same tool
                for neighbour in neighbours:
                    if neighbour.tool == node.tool:
                        weight = 1
                        node.edges.append((weight, neighbour))
                # add edges to itself to change tools
                for node_b in nodes[(x,y)]:
                    if node.tool != node_b.tool:
                        weight = 7
                        node.edges.append((weight, node_b)) # node_b -> node will be done later


    node_set = set()
    for node_list in nodes.values():
        for node in node_list:
            node_set.add(node)

    return dykstras(node_set, mouth, end)


def closest_node(node):
    return node.distance

def dykstras(nodes, start, end): # take nodes as set
    inf = 9999999
    for node in nodes:
        node.distance = inf
    start.distance = 0

    len_nodes = len(nodes)
    len_todo = len_nodes

    unvisited = [(start.distance, 0, start)] # first element distance for heapq sort

    # while not end.visited:
    while len(unvisited) > 0:
        _, _, current = heapq.heappop(unvisited)

        for edge in current.edges:
            dist = current.distance + edge[0]
            edge[1].distance = min(dist, edge[1].distance)
            tup = (edge[1].distance, edge[1].id, edge[1])
            if not edge[1].visited and tup not in unvisited:
                heapq.heappush(unvisited, tup)
        current.visited = True

    return end.distance

def print_cave(cave):
    for row in cave:
        str_row = list(map(str, row))
        print(''.join(str_row))

if __name__ == "__main__":
    print(main())
