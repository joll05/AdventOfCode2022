import re


f = open("input.txt")
input_raw = f.read().strip()
f.close()
input_lines = input_raw.splitlines()

PATTERN = r"^(addx|noop)(?: (-?\d+))?$"

X_register = 1
total_signal_strength = 0

cycle = 0
current_instruction = 0

CYCLE_TIMES = {
    "addx": 2,
    "noop": 1
}

# this code made sense to me at some point

while cycle <= 220:
    instruction = input_lines[current_instruction]
    match = re.match(PATTERN, instruction)
    operation = match.group(1)
    time = CYCLE_TIMES[operation]

    if (cycle + 20) // 40 < (cycle + time + 20) // 40:
        # like wtf is this
        register_cycle = (cycle + time + 20) // 40 * 40 - 20
        total_signal_strength += register_cycle * X_register
        print(cycle, register_cycle, X_register)
    
    if operation == "addx":
        number = int(match.group(2))
        X_register += number

    cycle += time
    
    current_instruction += 1

print(total_signal_strength)
