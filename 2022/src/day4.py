import os


def range_inclusive(start, end):
    return range(start, end + 1)


def solve(f):
    count = 0
    for line in f.read().split(os.linesep):
        e1, e2 = line.strip().split(",")
        e1 = set(range_inclusive(*map(int, e1.split("-"))))
        e2 = set(range_inclusive(*map(int, e2.split("-"))))
        if (e2 <= e1) | (e1 <= e2):
            count += 1
    return count


def solve2(f):
    count = 0
    for line in f.read().split(os.linesep):
        e1, e2 = line.strip().split(",")
        e1 = set(range_inclusive(*map(int, e1.split("-"))))
        e2 = set(range_inclusive(*map(int, e2.split("-"))))
        if len(e2 & e1) > 0:
            count += 1
    return count


filename = "../data/day4.input"
mode = "r"
f = open(filename, mode)
print(solve(f))
f.seek(0, 0)
print(solve2(f))
