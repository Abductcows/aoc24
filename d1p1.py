import re

from utils import run_with_file, get_input_for_day


def run(lines):
    left, right = [], []

    for line in lines:
        values = [int(e) for e in re.findall(r'\d+', line)]
        left.append(values[0])
        right.append(values[1])

    left.sort()
    right.sort()

    diff_sum = sum((abs(lval - rval) for lval, rval in zip(left, right)))
    return diff_sum


if __name__ == '__main__':
    print(run_with_file('example.txt', run))
    print(run(get_input_for_day('d1')))
