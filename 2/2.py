def read_lines(path):
    with open(path, "r") as f:
        line = f.readlines()
        return line

keypad = [["-", "-", "1", "-", "-"],
          ["-", "2", "3", "4", "-"],
          ["5", "6", "7", "8", "9"],
          ["-", "A", "B", "C", "-"],
          ["-", "-", "D", "-", "-"]]
x = 0
y = 2
code = []
lines = read_lines("input.txt")
for l in lines:
    for d in l:
        if d == "U":
            if y > 0:
                if keypad[y - 1][x] != "-":
                    y -= 1
        elif d == "D":
            if y < 4:
                if keypad[y + 1][x] != "-":
                    y += 1
        elif d == "L":
            if x > 0:
                if keypad[y][x - 1] != "-":
                    x -= 1
        elif d == "R":
            if x < 4:
                if keypad[y][x + 1] != "-":
                    x += 1
    code.append(str(keypad[y][x]))
result = "".join(code)
print result
