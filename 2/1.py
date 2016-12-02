def read_lines(path):
    with open(path, "r") as f:
        line = f.readlines()
        return line

keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x = 1
y = 1
code = []
lines = read_lines("input.txt")
for l in lines:
    for d in l:
        if d == "U":
            if y > 0:
                y -= 1
        elif d == "D":
            if y < 2:
                y += 1
        elif d == "L":
            if x > 0:
                x -= 1
        elif d == "R":
            if x < 2:
                x += 1
    code.append(str(keypad[y][x]))
result = "".join(code)
print result
