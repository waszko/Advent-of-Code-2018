
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, list):
        prev = None
        end = None
        for l in list:
            node = Node(l)
            node.prev = prev
            if prev:
                prev.next = node
            else:
                self.start = node
            end = node
        self.start.prev = end
        end.next = self.start
        self.current = self.start
        self.len = len(list)

    def get_next(self):
        self.current = self.current.next
        return self.current

    def get_prev(self):
        self.current = self.current.prev
        return self.current

    def insert(self, data):
        # insert after current
        node = Node(data)
        node.next = self.current.next
        node.prev = self.current
        node.next.prev = node
        self.current.next = node
        self.current = node
        self.len += 1

    def delete(self):
        prev = self.current.prev
        self.current = self.current.next
        self.current.prev = prev
        prev.next = self.current
        self.len -= 1

    def len(self):
        return self.len

    def __repr__(self):
        data = str(self.start.data)
        node = self.start.next
        while node != self.start:
            data += ", " + str(node.data)
            if node == self.current:
                data += "!"
            node = node.next
        return data

def main():
    players, last = 400, (71864 * 100)

    turn = 0
    scores = [0] * players
    marble = 0
    board = [0]
    board = LinkedList(board)

    while marble < last:
        marble += 1
        turn = (turn + 1) % players
        if marble % 23 != 0:
            board.get_next()
            board.insert(marble)
        else:
            scores[turn] += marble
            for i in range(7):
                remove = board.get_prev()
            scores[turn] += remove.data
            board.delete()
        # print(board)
    return max(scores)

if __name__ == "__main__":
    print(main())
