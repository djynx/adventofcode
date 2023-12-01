import re

digit_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
}

pattern = "(?=(" + "|".join(digit_dict.keys()) + "|[0-9]))"


def solve(f):
    numbers = []
    for line in f.read().split():
        digits = [i for i in line if i.isdigit()]
        numbers.append(int(digits[0] + digits[-1]))
    return sum(numbers)


def solve2(f):
    numbers = []
    for line in f.read().split():
        digits = [
            (item if item.isdigit() else digit_dict.get(item))
            for item in re.findall(pattern, line)
        ]
        numbers.append(int(digits[0] + digits[-1]))
    return sum(numbers)


filename = "../data/day1.input"
mode = "r"
f = open(filename, mode)
print(solve(f))
f.seek(0, 0)
print(solve2(f))
