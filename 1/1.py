def read_file(path):
    with open(path, "r") as f:
        line = f.readline()
        return line


def parse(line):
    return [(x.strip()[:1], x.strip()[1:]) for x in line.split(",")]

directions = ["N", "E", "S", "W"]
direction_index = 0
coords = [0, 0]

instructions = parse(read_file("input.txt"))
for i in instructions:
    if i[0] == "L":
        direction_index -= 1
    else:
        direction_index += 1
    direction_index %= len(directions)
    if directions[direction_index] == "N":
        coords[1] += int(i[1])
    elif directions[direction_index] == "S":
        coords[1] -= int(i[1])
    elif directions[direction_index] == "E":
        coords[0] += int(i[1])
    elif directions[direction_index] == "W":
        coords[0] -= int(i[1])

result = sum([abs(x) for x in coords])
print result
