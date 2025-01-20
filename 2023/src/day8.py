import math
import os
import re


def solve(f):
    map = {}
    instructions, maplines = f.read().split(2 * os.linesep)
    for line in maplines.split(os.linesep):
        line = re.findall(r"\w+", line)
        map[line[0]] = (line[1], line[2])
    curr = "AAA"
    count = 0
    while True:
        for instruction in instructions:
            if instruction == "L":
                curr = map[curr][0]
            else:
                curr = map[curr][1]
            count += 1
            if curr == "ZZZ":
                return count


def solve2(f):
    def find(map, instructions, start):
        count = 0
        while True:
            for instruction in instructions:
                # print("{0}:{1}:{2}".format(curr, map[curr], instruction), end="->")
                if instruction == "L":
                    start = map[start][0]
                else:
                    start = map[start][1]
                count += 1
                if start.endswith("Z"):
                    return count

    map = {}
    curr = []
    instructions, maplines = f.read().split(2 * os.linesep)
    for line in maplines.split(os.linesep):
        line = re.findall(r"\w+", line)
        map[line[0]] = (line[1], line[2])
        if line[0].endswith("A"):
            curr.append(line[0])
    for idx, item in enumerate(curr):
        curr[idx] = find(map, instructions, item)
    return math.lcm(*curr)


filename = "../data/day8.input"
mode = "r"
f = open(filename, mode)
print(solve(f))
f.seek(0, 0)
print(solve2(f))
