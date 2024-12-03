import re
from collections import defaultdict

from boilerplate import run_with_file, get_input_for_day


def run(lines):
    left, right = [], defaultdict(lambda: 0)

    for line in lines:
        values = [int(e) for e in re.findall(r'\d+', line)]
        left.append(values[0])
        right[values[1]] += 1

    similiarity_score = sum((value * right[value] for value in left))
    return similiarity_score


if __name__ == '__main__':
    print(run_with_file('example.txt', run))
    print(run(get_input_for_day('d1')))
