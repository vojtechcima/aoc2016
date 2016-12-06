def read_lines(path):
    lines = []
    with open(path, "r") as f:
        for l in f.readlines():
            lines.append(l.strip())
    return lines


def init_counters(n):
    counters = []
    for i in range(n):
        counters.append({})
    return counters


def get_min(d):
    return d.keys()[d.values().index(min(d.values()))]

lines = read_lines("input.txt")

counter = init_counters(len(lines[0]))
for l in lines:
    for ic in range(len(l)):
        if l[ic] not in counter[ic]:
            counter[ic][l[ic]] = 0
        counter[ic][l[ic]] += 1

result = "".join([get_min(c) for c in counter])

print result
