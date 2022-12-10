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

head_pos = [0, 0]
tail_pos = [0, 0]

tail_positions_visited = set()

for line in input_lines:
    match = re.match(PATTERN, line)
    direction = DIRECTIONS[match.group(1)]
    distance = int(match.group(2))

    for i in range(distance):
        head_pos[0] += direction[0]
        head_pos[1] += direction[1]

        if abs(head_pos[0] - tail_pos[0]) > 1 or abs(head_pos[1] - tail_pos[1]) > 1:
            tail_pos[0] += np.sign(head_pos[0] - tail_pos[0])
            tail_pos[1] += np.sign(head_pos[1] - tail_pos[1])

        tail_positions_visited.add(tuple(tail_pos))

print(len(tail_positions_visited))
