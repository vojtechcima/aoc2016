import numpy as np


def read_lines(path):
    with open(path, "r") as f:
        line = f.readlines()
        return line


def parse_line(l):
    parsed = l.split("-")
    id, checksum = parsed.pop().split("[")
    return (parsed, id, checksum.split("]")[0])


def decrypt_one(c, shift):
    return chr(ord("a") + ((ord(c) - ord("a") + shift) % (ord("z") - ord("a") + 1)))


def decrypt(data, shift):
    name = []
    for l in data:
        name.append("".join([decrypt_one(c, shift) for c in l]))
    return name

lines = read_lines("input.txt")
for l in lines:
    parsed = parse_line(l)
    if decrypt(parsed[0], int(parsed[1]))[0] == "northpole":
        result = parsed[1]

print result
