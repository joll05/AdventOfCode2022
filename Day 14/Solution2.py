f = open("input.txt")
input_raw = f.read().strip()
f.close()
input_lines = input_raw.splitlines()

blocks = set()
min_block = 0

for line in input_lines:
    points = line.split(" -> ")
    last_x = None
    last_y = None
    for point in points:
        x, y = point.split(",")
        x = int(x)
        y = int(y)

        if last_x != None and last_y != None:
            for cx in range(min(x, last_x), max(x, last_x) + 1):
                for cy in range(min(y, last_y), max(y, last_y) + 1):
                    blocks.add((cx, cy))
                    if cy > min_block:
                        min_block = cy
            
        last_x = x
        last_y = y

# print(blocks, min_block)

def simulate_sand(x, y):
    if y + 1 == min_block + 2:
        return (x, y)
    
    if (x, y + 1) not in blocks:
        return simulate_sand(x, y + 1)
    elif (x - 1, y + 1) not in blocks:
        return simulate_sand(x - 1, y + 1)
    elif (x + 1, y + 1) not in blocks:
        return simulate_sand(x + 1, y + 1)
    else:
        return (x, y)

START = (500, 0)

sand_count = 0

while True:
    result = simulate_sand(*START)

    sand_count += 1
    blocks.add(result)

    if result == START:
        break

print(sand_count)