f = open("input.txt")
input_raw = f.read().strip()
f.close()
input_lines = input_raw.splitlines()

priority_sum = 0

for group_number in range(len(input_lines) // 3):
    group = input_lines[group_number * 3: group_number * 3 + 3]

    intersection = set(group[0])

    for rucksack in group[1:]:
        intersection.intersection_update(rucksack)

    # list unpacking to find only element in set
    (item,) = intersection

    priority = ord(item.upper()) - ord('A') + 1

    if(item.isupper()):
        priority += 26    

    priority_sum += priority

print(priority_sum)