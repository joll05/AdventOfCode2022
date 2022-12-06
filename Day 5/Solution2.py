import re

f = open("input.txt")
input_raw = f.read()
f.close()
input_crates, input_instructions = input_raw.split("\n\n")
crates_lines = input_crates.splitlines()[:-1]
instruction_lines = input_instructions.strip().splitlines()

stacks = []

# if you're trying to understand how this works... fuck you, I'm not gonna bother commenting it
for i in range(1, len(crates_lines[0]), 4):
    stacks.append([])
    for line in crates_lines[::-1]:
        char = line[i]

        if char == ' ':
            break

        stacks[-1].append(char)

INSTRUCTION_PATTERN = r"^move (\d+) from (\d+) to (\d+)$"

for instruction in instruction_lines:
    match = re.match(INSTRUCTION_PATTERN, instruction)

    count = int(match.group(1))
    origin = int(match.group(2)) - 1
    destination = int(match.group(3)) - 1

    stacks[destination] += stacks[origin][-count:]
    stacks[origin] = stacks[origin][:-count]

for stack in stacks:    
    print(stack[-1], end="")

print()    
