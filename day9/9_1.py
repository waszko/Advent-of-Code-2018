
def main():
    # players, last = 9, 25
    # players, last = 10, 1618
    # players, last = 13, 7999
    # players, last = 17, 1104
    # players, last = 21, 6111
    # players, last = 30, 5807
    players, last = 400, 71864

    turn = 0
    scores = [0] * players
    marble = 0
    board = [0]
    current = 0

    while marble < last:
        marble += 1
        turn = (turn + 1) % players
        if marble % 23 != 0:
            left_pos = (current + 1) % len(board)
            new_pos = (left_pos + 1)
            board.insert(new_pos, marble)
            current = new_pos
        else:
            scores[turn] += marble
            remove = (current - 7) % len(board)
            scores[turn] += board[remove]
            del board[remove]
            current = remove
        # print(board)
    return max(scores)

if __name__ == "__main__":
    print(main())
