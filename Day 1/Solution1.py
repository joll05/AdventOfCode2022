f = open("input.txt")
input_raw = f.read().strip()
f.close()
input_sections = input_raw.split("\n\n")

elves = []

for elf in input_sections:
    elves += [0]
    for number in elf.split("\n"):
        elves[-1] += int(number)

print(max(elves))
