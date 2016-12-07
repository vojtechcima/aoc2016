def read_lines(path):
    lines = []
    with open(path, "r") as f:
        for l in f.readlines():
            lines.append(l.strip())
    return lines


def parse_line(line):
    inner_parts = []
    outer_parts = []
    l_split = line.split("[")
    if l_split[0]:
        outer_parts.append(l_split[0])
    for i in range(1, len(l_split)):
        r_split = l_split[i].split("]")
        inner_parts.append(r_split[0])
        outer_parts.append(r_split[1])
    return (inner_parts, outer_parts)


def validate(inner_parts, outer_parts):
    triplets = []
    for p in outer_parts:
        for i in range(len(p) - 2):
            if p[i] == p[i + 2] and p[i] != p[i + 1]:
                triplets.append(p[i + 1] + p[i] + p[i + 1])
    for t in triplets:
        for p in inner_parts:
            if p.find(t) != -1:
                return True

    return False


def parse_lines(lines):
    parsed = []
    for l in lines:
        parsed.append(parse_line(l))
    return parsed

counter = 0
lines = read_lines("input.txt")
parsed_lines = parse_lines(lines)
for l in parsed_lines:
    if validate(l[0], l[1]):
        counter += 1
result = counter
print result
