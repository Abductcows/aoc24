from collections import defaultdict


def get_lines(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip('\n'))

    while lines and not lines[-1]:
        lines.pop()

    return lines


import re


def run(filename):
    lines = get_lines(filename)

    left, right = [], defaultdict(lambda : 0)

    for line in lines:
        values = [int(e) for e in re.findall(r'\d+', line)]
        left.append(values[0])
        right[values[1]] = right[values[1]] + 1

    similiarity_score = 0
    for value in left:
        similiarity_score += value * right[value]

    print(similiarity_score)


if __name__ == '__main__':
    run('example.txt')
    run('input.txt')
