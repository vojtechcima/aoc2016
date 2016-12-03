import numpy as np


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
parsed_lines = []
for l in lines:
    parsed_lines.append(parse_line(l))
array = np.array(parsed_lines)
vec = np.reshape(array.T, 3 * len(parsed_lines))
for i in range(0, len(vec), 3):
    if triangle([vec[i], vec[i + 1], vec[i + 2]]):
        counter += 1

result = counter
print result
