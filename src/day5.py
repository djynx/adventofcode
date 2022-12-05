import os
from re import findall
from collections import deque
import itertools


def parse_stacks_and_moves(f):
    stacks = []
    crates, moves = f.read().split(2 * os.linesep)
    for line in crates.splitlines()[:-1]:
        for index, position in enumerate(range(1, len(line), 4)):
            if len(stacks) <= index:
                stacks.append(deque())
            if line[position] != " ":
                stacks[index].extendleft(line[position])
    return stacks, moves


def solve(f):
    out = ""
    stacks, moves = parse_stacks_and_moves(f)
    for move in moves.splitlines():
        count, source, destination = map(int, findall(r"\d+", move))
        for i in range(int(count)):
            stacks[destination - 1].append(stacks[source - 1].pop())
    for stack in stacks:
        out += stack.pop()
    return out


def solve2(f):
    out = ""
    stacks, moves = parse_stacks_and_moves(f)
    for move in moves.splitlines():
        count, source, destination = map(int, findall(r"\d+", move))
        temp = deque()
        for i in range(count):
            temp.appendleft(stacks[source - 1].pop())
        stacks[destination - 1].extend(temp)
    for stack in stacks:
        out += stack.pop()
    return out


filename = "../data/day5.input"
mode = "r"
f = open(filename, mode)
print(solve(f))
f.seek(0, 0)
print(solve2(f))
