def read_lines(path):
    with open(path, "r") as f:
        lines = f.readlines()
        return lines


def parse_line(line, delimeter=" "):
    return [int(x.strip()) for x in line.split(delimeter) if x]


def triangle(l):
    print l
    for i in range(3):
        if l[i % 3] + l[(i + 1) % 3] <= l[(i + 2) % 3]:
            return False
    return True
lines = read_lines("input.txt")

counter = 0
for l in lines:
    if triangle(parse_line(l)):
        counter += 1

result = counter
print result
