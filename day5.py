
from rich import print
import re

import sys
MOVE_RE = "move ([0-9]*) from ([0-9]*) to ([0-9]*)"
CMP_MOV_RE = re.compile(MOVE_RE)

def print_queues(queues):
    for idx, q in enumerate(queues):
        print(f"Queue #{idx}: ", end="")
        print(q)


def main():
    data =     """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

    with open("day5_input.txt", 'r') as fp:
        data = fp.read()

    rows = data.split("\n")
    moves = list()

    queues = list()
    crates_index = -1
    for c in range(1, len(rows[0]), 4):
        queues.append(list())
        for r in range(0, len(rows)):
            if rows[r] == '' or rows[r][c] == ' ':
                continue
            #print(rows[r][c])

            if rows[r][c].isdigit():
                print(f"Found stack #{rows[r][c]}")
                crates_index = r + 2
                break

            queues[-1].insert(0, rows[r][c])
    print_queues(queues)

    for row in rows[crates_index:]:
        if row == '':
            continue
        m = re.search(CMP_MOV_RE, row)
        moves.append(m.groups())

    for move in moves:
        mover_list = list()
        num = int(move[0])
        from_idx = int(move[1]) - 1
        to_idx = int(move[2]) - 1

        for x in range(0, num):
            if len(queues[from_idx]) == 0:

                return 0
            box = queues[from_idx].pop()
            mover_list.append(box)

        for _ in range(0, len(mover_list)):
            queues[to_idx].append(mover_list.pop())

    print_queues(queues)

    for q in queues:
        if len(q) == 0:
            continue
        print(q.pop(), end='')

    print("")

if __name__ == "__main__":
    main()