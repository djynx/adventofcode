import os
import re


def calc_ways(time: int, record: int):
    ans = 0
    for i in range(1, time):
        if record < i * (time - i):
            ans += 1
    return ans


def solve(f):
    lines = f.read().split(os.linesep)
    ans = 1
    for idx, line in enumerate(lines):
        lines[idx] = re.findall(r"\d+", line)
    for i in range(len(lines[0])):
        ans *= calc_ways(int(lines[0][i]), int(lines[1][i]))
    return ans


def solve2(f):
    lines = f.read().split(os.linesep)
    for idx, line in enumerate(lines):
        lines[idx] = re.findall(r"\d+", line)
    return calc_ways(int("".join(lines[0])), int("".join(lines[1])))


filename = "../data/day6.input"
mode = "r"
f = open(filename, mode)
print(solve(f))
f.seek(0, 0)
print(solve2(f))
