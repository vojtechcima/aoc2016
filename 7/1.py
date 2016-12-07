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
    for p in inner_parts:
        for i in range(1, len(p) - 2):
            if p.find(p[i - 1:i + 1] + "".join(reversed(p[i - 1:i + 1]))) != -1 and p[i] != p[i - 1]:
                # found where not supposed to find
                return False
    for p in outer_parts:
        for i in range(1, len(p) - 2):
            if p.find(p[i - 1:i + 1] + "".join(reversed(p[i - 1:i + 1]))) != -1 and p[i] != p[i - 1]:
                # found where it supposed to find
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
