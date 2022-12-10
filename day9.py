from copy import copy
from typing import List, Optional


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, obj):
        return isinstance(obj, Point) and obj.x == self.x and obj.y == self.y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()

    def is_adjacent(self, other):
        x_distance = abs(other.x - self.x)
        y_distance = abs(other.y - self.y)

        return x_distance <= 1 and y_distance <= 1


class Node(object):
    def __init__(self, x: int, y: int, name: str):
        self.loc = Point(x, y)
        self.name = name

    def move(self, direction):
        raise Exception("Cannot move a node.")


class Head(Node):
    def __init__(self, x, y, name):
        super().__init__(x, y, name)

    def move(self, direction):
        if direction == 'U':
            self.loc.y -= 1
        elif direction == 'D':
            self.loc.y += 1
        elif direction == 'L':
            self.loc.x -= 1
        elif direction == 'R':
            self.loc.x += 1


class Tail(Node):
    def __init__(self, x: int, y: int, name: str):
        super().__init__(x, y, name)
        self.positions = list()
        self.positions.append(copy(self.loc))
        self.head = None

    def set_head(self, head):
        self.head = head

    def move(self, direction):

        if self.head.loc == self.loc:
            return
        if self.loc.is_adjacent(self.head.loc):
            return

        if self.loc.x < self.head.loc.x and self.loc.y == self.head.loc.y:
            self.loc.x += 1
        elif self.loc.x > self.head.loc.x and self.loc.y == self.head.loc.y:
            self.loc.x -= 1
        elif self.loc.x == self.head.loc.x and self.loc.y < self.head.loc.y:
            self.loc.y += 1
        elif self.loc.x == self.head.loc.x and self.loc.y > self.head.loc.y:
            self.loc.y -= 1
        elif self.loc.x < self.head.loc.x and self.loc.y < self.head.loc.y:
            self.loc.x += 1
            self.loc.y += 1
        elif self.loc.x > self.head.loc.x and self.loc.y > self.head.loc.y:
            self.loc.x -= 1
            self.loc.y -= 1
        elif self.loc.x < self.head.loc.x and self.loc.y > self.head.loc.y:
            self.loc.y -= 1
            self.loc.x += 1
        elif self.loc.x > self.head.loc.x and self.loc.y < self.head.loc.y:
            self.loc.y += 1
            self.loc.x -= 1
        else:
            print(
                f"Error: Something not taken into account! Me: ({self.loc.x}, {self.loc.y}) Head: ({self.head.loc.x}, {self.head.loc.y})")

        if self.loc not in self.positions:
            self.positions.append(copy(self.loc))


def knot_at_point(knots: List[Node], point: Point) -> Optional[Node]:
    for knot in knots:
        if knot.loc == point:
            return knot
    return None


def print_grid(knots: List[Node]):
    for r in range(0, 21):
        for c in range(0, 26):
            knot: Node = knot_at_point(knots, Point(c, r))
            if knot is None:
                print(".", end='')
            else:
                print(knot.name, end='')
        print("")
    print("")


def execute_instruction(direction: str, num: int, knots: List[Node]):
    for x in range(0, num):
        for knot in knots:
            knot.move(direction)


def main():
    data = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''
    data = '''R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20'''

    with open("day9_input.txt", 'r') as fp:
        data = fp.read()

    knots = list()
    start_point = Point(11, 15)
    head = Head(start_point.x, start_point.y, 'H')
    knots.append(head)
    for x in range(0, 9):
        t = Tail(start_point.x, start_point.y, str(x + 1))
        t.set_head(knots[-1])
        knots.append(t)

    knots[-1].name = 'T'

    print(head.loc)
    for line in data.split("\n"):
        direction, number = line.split(' ')
        number = int(number)

        # print(f"Direction: {direction} Number of spaces: {number}")
        execute_instruction(direction, number, knots)

    print(f"Unique positions {len(knots[-1].positions)}")


if __name__ == "__main__":
    main()