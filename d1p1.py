import re

from boilerplate import get_lines


def run(filename):
    lines = get_lines(filename)

    left, right = [], []

    for line in lines:
        values = [int(e) for e in re.findall(r'\d+', line)]
        left.append(values[0])
        right.append(values[1])

    left.sort()
    right.sort()

    diff_sum = sum((abs(lval - rval) for lval, rval in zip(left, right)))
    print(diff_sum)
    return diff_sum


if __name__ == '__main__':
    run('example.txt')
    run('input.txt')
