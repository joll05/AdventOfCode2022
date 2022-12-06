f = open("input.txt")
input_raw = f.read().strip()
f.close()

for i in range(4, len(input_raw)):
    window = input_raw[i-4:i]
    if len(set(window)) == 4:
        print(i)
        break