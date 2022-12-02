f = open("input.txt")
input_raw = f.read().strip()
f.close()
input_lines = input_raw.split("\n")

def shape_to_int(shape):
    match shape:
        case "A" | "X":
            return 0
        case "B" | "Y":
            return 1
        case "C" | "Z":
            return 2
    
    return -1

total_score = 0

for round in input_lines:
    opponent, player = shape_to_int(round[0]), shape_to_int(round[2])
    
    total_score += player + 1
    
    if (player + 2) % 3 == opponent:
        # win
        total_score += 6
    elif player == opponent:
        # draw
        total_score += 3

print(total_score)
