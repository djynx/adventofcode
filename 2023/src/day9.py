def history_tree(history):
    history_tree = [[int(x) for x in history]]
    last = history_tree[-1]
    while len(set(last)) != 1:
        reversed_hist = list(reversed(last))
        diffs = []
        for i in range(len(last) - 1):
            diffs.append(reversed_hist[i] - reversed_hist[i + 1])
        history_tree.append(list(reversed(diffs)))
        last = history_tree[-1]
    return history_tree


def solve(f):
    def next(history):
        return sum([item[-1] for item in history_tree(history)])

    ans = 0
    for history in f.readlines():
        ans += next(history.split())
    return ans


def solve2(f):
    def prev(history):
        reversed_hist = list(reversed(history_tree(history)))
        for i in range(len(reversed_hist) - 1):
            reversed_hist[i + 1].insert(
                0, reversed_hist[i + 1][0] - reversed_hist[i][0]
            )
        return reversed_hist[-1][0]

    ans = 0
    for history in f.readlines():
        ans += prev(history.split())
    return ans


filename = "../data/day9.input"
mode = "r"
f = open(filename, mode)
print(solve(f))
f.seek(0, 0)
print(solve2(f))
