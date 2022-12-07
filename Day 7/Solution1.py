import re

f = open("input.txt")
input_raw = f.read().strip()
f.close()
input_lines = input_raw.splitlines()

class Directory:
    def __init__(self, parent, name : str) -> None:
        self.parent = parent
        self.subdirs = {}
        self.files = {}
        self.size = 0

        if parent != None:
            parent.subdirs[name] = self
    
    def add_file(self, file):
        self.files[file.name] = file
        self.add_to_size(file.size)

    def add_to_size(self, size : int):
        self.size += size
        if self.parent != None:
            self.parent.add_to_size(size)


class File:
    def __init__(self, name : str, size : int, directory : Directory) -> None:
        self.name = name
        self.size = size

        directory.add_file(self)

root = Directory(None, "")

current_directory = root

COMMAND_PATTERN = r"^\$ ([a-z]+)(?: ([a-z/.]+))?$"
LS_PATTERN = r"^(dir|\d+) ([a-z.]+)$"

for line in input_lines:
    command_match = re.match(COMMAND_PATTERN, line)

    if command_match:
        command = command_match.group(1)
        argument = command_match.group(2)
        if command == "cd":
            if argument == "/":
                current_directory = root
            elif argument == "..":
                current_directory = current_directory.parent
            else:
                current_directory = current_directory.subdirs[argument]
    else:
        ls_match = re.match(LS_PATTERN, line)
        dir_or_size = ls_match.group(1)
        name = ls_match.group(2)
        if dir_or_size == "dir":
            Directory(current_directory, name)
        else:
            size = int(dir_or_size)
            File(name, size, current_directory)

def calculate_removable_space(directory : Directory):
    total = 0

    if directory.size <= 100_000:
        total += directory.size
    
    for subdir in directory.subdirs.values():
        total += calculate_removable_space(subdir)
    
    return total

print(calculate_removable_space(root))
