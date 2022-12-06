f = open("input.txt")
input_raw = f.read().strip()
f.close()

# I feel like this was meant to be an optimization challenge, but this does just work

for i in range(14, len(input_raw)):
    window = input_raw[i-14:i]
    if len(set(window)) == 14:
        print(i)
        break