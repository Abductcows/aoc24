from utils import get_lines, get_input_for_day, runtime


def digits(n, length):
    mask = 10 ** (length - 1)
    for _ in range(length):
        q, r = divmod(n, mask)
        yield q
        mask //= 10
        n = r


def first(l, target, key):
    for i, e in enumerate(l):
        if key(e) == target:
            return i
    return -1


height = 7
width = 5


@runtime
def run(lines):
    items = [lines[i:i + height] for i in range(0, len(lines), height + 1)]
    keys, locks = [], []

    for item in items:
        val = 0
        if item[0][0] == '#':
            for i in range(width):
                val = 10 * val - 1 + first(item, '.', lambda e: e[i])
            locks.append(val)
        else:
            for i in range(width):
                val = 10 * val + height - 1 - first(item, '#', lambda e: e[i])
            keys.append(val)

    total = 0

    for key in keys:
        for lock in locks:
            fits = True
            for digit_pair in zip(digits(key, width), digits(lock, width)):
                if sum(digit_pair) >= height - 1:
                    fits = False
                    break
            if fits:
                total += 1

    return total

if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d25')))