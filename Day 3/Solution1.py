f = open("input.txt")
input_raw = f.read().strip()
f.close()
input_lines = input_raw.splitlines()

priority_sum = 0

for rucksack in input_lines:
    divider = len(rucksack) // 2
    compartment_1, compartment_2 = set(rucksack[divider:]), set(rucksack[:divider])
    intersection = compartment_1.intersection(compartment_2)

    for item in intersection:
        priority = ord(item.upper()) - ord('A') + 1

        if(item.isupper()):
            priority += 26
        

        priority_sum += priority

print(priority_sum)