import re
from collections import defaultdict

from boilerplate import get_lines


def run(filename):
    lines = get_lines(filename)

    left, right = [], defaultdict(lambda: 0)

    for line in lines:
        values = [int(e) for e in re.findall(r'\d+', line)]
        left.append(values[0])
        right[values[1]] += 1

    similiarity_score = sum((value * right[value] for value in left))
    print(similiarity_score)
    return similiarity_score


if __name__ == '__main__':
    run('example.txt')
    run('input.txt')
