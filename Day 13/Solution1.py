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

index_sum = 0

for i, pair in enumerate(input_sections, start=1):
    left, right = pair.splitlines()

    # I know eval is unsafe, but I don't really care, this is easy
    left = eval(left)
    right = eval(right)

    comparison_result = compare(left, right)
    if comparison_result == 1:
        index_sum += i

print(index_sum)