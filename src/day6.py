def solve(f):
    txt = f.read()
    for x in range(4, len(txt)):
        if len(set(txt[x - 4:x])) == 4:
            return x


def solve2(f):
    txt = f.read()
    for x in range(14, len(txt)):
        if len(set(txt[x - 14:x])) == 14:
            return x


filename = "../data/day6.input"
mode = "r"
f = open(filename, mode)
print(solve(f))
f.seek(0, 0)
print(solve2(f))
