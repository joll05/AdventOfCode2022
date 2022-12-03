f = open("input.txt")
input_raw = f.read().strip()
f.close()
input_lines = input_raw.splitlines()

def char_to_int(shape):
    match shape:
        case "A" | "X":
            return 0
        case "B" | "Y":
            return 1
        case "C" | "Z":
            return 2
    
    return -1

total_score = 0

# hey, I realise this code is confusing af, but I'm not gonna bother making it more readable ¯\_(ツ)_/¯
for round in input_lines:
    opponent, outcome = char_to_int(round[0]), char_to_int(round[2])
    
    total_score += outcome * 3
    
    your_shape = (opponent + outcome - 1) % 3

    total_score += your_shape + 1

print(total_score)
