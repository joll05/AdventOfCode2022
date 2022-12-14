from functools import cmp_to_key

def compare(left : list | int, right : list | int) -> int:
    if type(left) == int and type(right) == int:
        return 1 if left < right else 0 if left == right else -1
    elif type(left) == int:
        left = [left]
    elif type(right) == int:
        right = [right]
    
    for i in range(len(left)):
        if i >= len(right):
            return -1
        
        left_val = left[i]
        right_val = right[i]
        
        compare_result = compare(left_val, right_val)
        if compare_result != 0:
            return compare_result
    
    if len(left) < len(right):
        return 1
    
    return 0

f = open("input.txt")
input_raw = f.read().strip()
f.close()
input_sections = input_raw.split("\n\n")

packets = [[[2]], [[6]]]

for i, pair in enumerate(input_sections, start=1):
    left, right = pair.splitlines()

    # I know eval is unsafe, but I don't really care, this is easy
    packets.append(eval(left))
    packets.append(eval(right))

packets : list = sorted(packets, key=cmp_to_key(compare), reverse=True)

print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))