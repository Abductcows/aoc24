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

    left, right = [], []
    for line in lines:
        values = [int(e) for e in re.findall(r'\d+', line)]
        left.append(values[0])
        right.append(values[1])

    left.sort()
    right.sort()

    diff_sum = 0
    for lval, rval in zip(left, right):
        diff_sum += abs(lval - rval)

    print(diff_sum)


if __name__ == '__main__':
    run('example.txt')
    # run('input.txt')
