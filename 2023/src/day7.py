from collections import Counter


def solve(f):
    letter_map = {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}

    def type(card):
        card = Counter(card)
        match len(card):
            case 5:
                return 0
            case 4:
                return 1
            case 3:
                if 3 in card.values():
                    return 3
                else:
                    return 2
            case 2:
                if 4 in card.values():
                    return 5
                else:
                    return 4
            case 1:
                return 6

    hands = []
    for line in f.readlines():
        cards = line.split()[0]
        point = line.split()[1]
        hands.append(
            (type(cards), [letter_map.get(card, card) for card in cards], point)
        )
    hands = sorted(hands)
    sum = 0
    for idx, hand in enumerate(hands):
        sum += (idx + 1) * int(hand[2])

    return sum


def solve2(f):
    letter_map = {"T": "A", "J": ".", "Q": "C", "K": "D", "A": "E"}

    def type(card):
        if card == "JJJJJ":
            return 6
        card = Counter(card)
        j_count = card.pop("J", 0)
        card[card.most_common(1)[0][0]] += j_count
        match len(card):
            case 5:
                return 0
            case 4:
                return 1
            case 3:
                if 3 in card.values():
                    return 3
                else:
                    return 2
            case 2:
                if 4 in card.values():
                    return 5
                else:
                    return 4
            case 1:
                return 6

    hands = []
    for line in f.readlines():
        cards = line.split()[0]
        point = line.split()[1]
        hands.append(
            (type(cards), [letter_map.get(card, card) for card in cards], point)
        )
    hands = sorted(hands)
    sum = 0
    for idx, hand in enumerate(hands):
        sum += (idx + 1) * int(hand[2])

    return sum


filename = "../data/day7.input"
mode = "r"
f = open(filename, mode)
print(solve(f))
f.seek(0, 0)
print(solve2(f))
