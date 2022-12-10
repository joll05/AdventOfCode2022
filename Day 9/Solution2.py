import re
import numpy as np

f = open("input.txt")
input_raw = f.read().strip()
f.close()
input_lines = input_raw.splitlines()

PATTERN = r"^(U|D|L|R) (\d+)$"

DIRECTIONS = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (1, 0)
}

tail_positions_visited = {(0, 0)}

class knot:
    def __init__(self, tail):
        self.pos = [0, 0]
        self.tail = tail
    
    def move_knot(self, direction, distance, do_print=False):
        global tail_positions_visited

        for _ in range(distance):
            self.pos[0] += direction[0]
            self.pos[1] += direction[1]

            if self.tail != None and (abs(self.pos[0] - self.tail.pos[0]) > 1 or abs(self.pos[1] - self.tail.pos[1]) > 1):
                x_movement = np.sign(self.pos[0] - self.tail.pos[0])
                y_movement = np.sign(self.pos[1] - self.tail.pos[1])
                self.tail.move_knot((x_movement, y_movement), 1)
        
        if self.tail == None:
            tail_positions_visited.add(tuple(self.pos))

head = None

for _ in range(10):
    head = knot(head)

for line in input_lines:
    match = re.match(PATTERN, line)
    direction = DIRECTIONS[match.group(1)]
    distance = int(match.group(2))

    head.move_knot(direction, distance, True)

print(len(tail_positions_visited))
    