import re

f = open("input.txt")
input_raw = f.read().strip()
f.close()
input_lines = input_raw.splitlines()

pattern = r'^(\d+)-(\d+),(\d+)-(\d+)$'

overlaps = 0

for pair in input_lines:
    match = re.match(pattern, pair)
    min1, max1 = int(match.group(1)), int(match.group(2))
    min2, max2 = int(match.group(3)), int(match.group(4))

    if (min2 <= min1 <= max2) or (min2 <= max1 <= max2) or (min1 <= min2 <= max1) or (min1 <= max2 <= max1):
        overlaps += 1

print(overlaps)
