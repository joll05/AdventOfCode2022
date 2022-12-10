import re


f = open("input.txt")
input_raw = f.read().strip()
f.close()
input_lines = input_raw.splitlines()

PATTERN = r"^(addx|noop)(?: (-?\d+))?$"

sprite_positions = [1]

for instruction in input_lines:
    match = re.match(PATTERN, instruction)
    operation = match.group(1)

    sprite_positions.append(sprite_positions[-1])
    print(operation)
    if operation == "addx":
        number = int(match.group(2))
        sprite_positions.append(sprite_positions[-1] + number)

# this code made sense to me at some point

print(sprite_positions)

render = "+" + "-" * 40 + "+\n"

for row in range(6):
    render += "|"
    for col in range(40):
        cycle = row * 40 + col

        print(cycle)

        if abs(col - sprite_positions[cycle]) <= 1:
            render += "#"
        else:
            render += " "
    render += "|\n"

render += "+" + "-" * 40 + "+"

print(render)