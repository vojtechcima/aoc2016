import numpy as np
np.set_printoptions(linewidth=1000)


def read_lines(path):
    lines = []
    with open(path, "r") as f:
        for l in f.readlines():
            lines.append(l.strip())
    return lines


def parse_line(line):
    l = line.split()
    parsed = []
    if l[0] == "rect":
        parsed = [l[0]] + l[1].split("x")
    elif l[0] == "rotate":
        parsed = [l[0], l[1], l[2].split("=")[1], l[4]]
    return parsed


def parse_lines(lines):
    parsed_lines = []
    for l in lines:
        parsed_lines.append(parse_line(l))
    return parsed_lines


def rect(screen, width, height):
    for y in range(height):
        for x in range(width):
            screen[y][x] = 1


def rot_row(screen, index, s):
    shifted = np.zeros(len(screen[index]))
    for i in range(len(screen[index])):
        shifted[(i + s) % len(screen[index])] = screen[index][i]
    for i in range(len(screen[index])):
        screen[index][i] = shifted[i]


def rot_col(screen, index, s):
    shifted = np.zeros(len(screen))
    for i in range(len(screen)):
        shifted[(i + s) % len(screen)] = screen[i][index]
    for i in range(len(screen)):
        screen[i][index] = shifted[i]


WIDTH = 50
HEIGHT = 6
screen = np.zeros((HEIGHT, WIDTH))
lines = read_lines("input.txt")
parsed_lines = parse_lines(lines)
for i in parsed_lines:
    if i[0] == "rect":
        rect(screen, int(i[1]), int(i[2]))
    elif i[0] == "rotate":
        if i[1] == "row":
            rot_row(screen, int(i[2]), int(i[3]))
        elif i[1] == "column":
            rot_col(screen, int(i[2]), int(i[3]))

counter = 0
for y in range(HEIGHT):
    for x in range(WIDTH):
        if screen[y][x] == 1:
            counter += 1

result = counter
print result
