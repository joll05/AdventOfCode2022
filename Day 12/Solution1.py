from functools import lru_cache
import numpy as np

f = open("input.txt")
input_raw = f.read().strip()
f.close()
input_lines = input_raw.splitlines()

heights : np.ndarray = np.zeros((len(input_lines[0]), len(input_lines)))
start = None
end = None

for y, line in enumerate(input_lines):
    for x, char in enumerate(line):
        height = ord(char) - ord("a")

        if char == "S":
            height = 0
            start = (x, y)
        elif char == "E":
            height = 25
            end = (x, y)
        
        heights[x, y] = height

NEIGHBORS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def get_shortest_path(start, end, heights : np.ndarray):
    distance = 0

    current_locations = [start]

    visited_locations = set(current_locations)

    while True:
        new_locations = []
        
        for location in current_locations:
            if location == end:
                return distance

            for neighbor in NEIGHBORS:
                x = location[0] + neighbor[0]
                y = location[1] + neighbor[1]

                if (x, y) in visited_locations:
                    continue

                in_bounds = 0 <= x < heights.shape[0] and 0 <= y < heights.shape[1]
                if in_bounds and heights[location] >= heights[x, y] - 1:
                    new_locations.append((x, y))
                    visited_locations.add((x, y))
        
        current_locations = new_locations
        distance += 1

print(get_shortest_path(start, end, heights))


