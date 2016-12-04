import numpy as np


def read_lines(path):
    with open(path, "r") as f:
        line = f.readlines()
        return line


def parse_line(l):
    parsed = l.split("-")
    id, checksum = parsed.pop().split("[")
    return (parsed, id, checksum.split("]")[0])


def compute_checksum(d):
    res = ""
    for v in sorted(set(d.values()), reverse=True):
        res += "".join(sorted([k for k in d.keys() if d[k] == v]))
    return res[:5]


def count_letters(data):
    d = {}
    for l in data:
        for c in l:
            if c not in d:
                d[c] = 0
            d[c] += 1
    return d

lines = read_lines("input.txt")
total = 0
for l in lines:
    parsed = parse_line(l)
    counted_letters = count_letters(parsed[0])
    checksum = compute_checksum(counted_letters)
    if checksum == parsed[2]:
        total += int(parsed[1])

result = total
print result
