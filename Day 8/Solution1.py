f = open("input.txt")
input_raw = f.read().strip()
f.close()
input_lines = input_raw.splitlines()

heights = []

for line in input_lines:
    heights.append([])

    for char in line:
        heights[-1].append(int(char))

def is_visible(heights, x, y):
    for direction in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        height = heights[y][x]

        current_x = x
        current_y = y
        
        do_continue = True
        
        while do_continue:
            current_x += direction[0]
            current_y += direction[1]

            if not (0 <= current_y < len(heights) and 0 <= current_x < len(heights[0])):
                # reached the treeline
                return True

            do_continue = heights[current_y][current_x] < height
            
    return False
        

visible_count = 0

for y, row in enumerate(heights):
    for x in range(len(row)):
        if is_visible(heights, x, y):
            visible_count += 1

print(visible_count)