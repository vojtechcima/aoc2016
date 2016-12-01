def read_file(path):
    with open(path, "r") as f:
        line = f.readline()
        return line


def parse(line):
    return [(x.strip()[:1], x.strip()[1:]) for x in line.split(",")]

directions = ["N", "E", "S", "W"]
direction_index = 0
coords = [0, 0]
coords_log = []
instructions = parse(read_file("input.txt"))
found = False
for i in instructions:

    if i[0] == "L":
        direction_index -= 1
    else:
        direction_index += 1
    direction_index %= len(directions)
    for s in range(int(i[1])):
        if directions[direction_index] == "N":
            coords[1] += 1
        elif directions[direction_index] == "S":
            coords[1] -= 1
        elif directions[direction_index] == "E":
            coords[0] += 1
        elif directions[direction_index] == "W":
            coords[0] -= 1
        if coords in coords_log:
            found = True
            break
        coords_log.append([coords[0], coords[1]])
    if found:
        break

result = sum([abs(x) for x in coords])
print result
