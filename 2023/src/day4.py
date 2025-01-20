def solve(f):
    ans = 0
    for idx, line in enumerate(f.readlines()):
        _, game = line.rstrip().split(": ")
        elf, player = game.split(" | ")
        amount = len(list(set(elf.split()) & set(player.split())))
        if amount > 0:
            ans += 2 ** (amount - 1)
    return ans


def solve2(f):
    dict = {}
    for idx, line in enumerate(f.readlines()):
        dict.setdefault(idx, 1)
        _, game = line.rstrip().split(": ")
        elf, player = game.split(" | ")
        amount = len(list(set(elf.split()) & set(player.split())))
        for i in range(idx + 1, idx + amount + 1):
            dict[i] = dict.get(i, 1) + dict[idx]

    return sum(dict.values())


filename = "../data/day4.input"
mode = "r"
f = open(filename, mode)
print(solve(f))
f.seek(0, 0)
print(solve2(f))
