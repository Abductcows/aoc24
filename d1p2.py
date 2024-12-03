import re
from collections import defaultdict

from boilerplate import run_with_file, lines_getter


def run(lines):
    left, right = [], defaultdict(lambda: 0)

    for line in lines:
        values = [int(e) for e in re.findall(r'\d+', line)]
        left.append(values[0])
        right[values[1]] += 1

    similiarity_score = sum((value * right[value] for value in left))
    print(similiarity_score)
    return similiarity_score


if __name__ == '__main__':
    run_with_file('example.txt', run)
    run(lines_getter('d1'))
