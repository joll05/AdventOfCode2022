import re


f = open("input.txt")
input_raw = f.read().strip()
f.close()
input_sections = input_raw.split("\n\n")

class monkey:
    def __init__(self, items : list, operand : str, operation_value : int, self_multiplication : bool, test_value : int, true_monkey : int, false_monkey : int):
        self.items = items

        self.operation = lambda x: (x + operation_value) if operand == '+' else (x * (x if self_multiplication else operation_value))

        self.test_value = test_value
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey

        self.inspections = 0
    
    def get_moves(self):
        moves = {}

        for item in self.items:
            value = self.operation(item)
            target_monkey = self.true_monkey if value % self.test_value == 0 else self.false_monkey

            if target_monkey not in moves:
                moves[target_monkey] = [value]
            else:
                moves[target_monkey].append(value)
            
            self.inspections += 1
        
        return moves


PATTERN = r"""^Monkey (\d+):
  Starting items: (\d+(?:,\s\d+)*)
  Operation: new = old (\+|\*) (\d+|old)
  Test: divisible by (\d+)
    If true: throw to monkey (\d+)
    If false: throw to monkey (\d+)$"""

monkeys = []

max_divisor = 1

for section in input_sections:
    match = re.match(PATTERN, section)
    items = [int(n) for n in match.group(2).split(", ")]
    operand = match.group(3)
    operation_value = match.group(4)
    self_multiplication = operation_value == "old"
    operation_value = int(operation_value) if not self_multiplication else 0
    test_value = int(match.group(5))

    max_divisor *= test_value

    true_monkey = int(match.group(6))
    false_monkey = int(match.group(7))

    monkeys.append(monkey(items, operand, operation_value, self_multiplication, test_value, true_monkey, false_monkey))


for _ in range(10000):
    for this_monkey in monkeys:
        moves = this_monkey.get_moves()
    
        for i, move in moves.items():
            move = [m % max_divisor for m in move]
            monkeys[i].items.extend(move)
        
        this_monkey.items = []
    
    print(_)

sorted_monkeys = sorted(monkeys, key=lambda x: x.inspections, reverse=True)
print(sorted_monkeys[0].inspections * sorted_monkeys[1].inspections)