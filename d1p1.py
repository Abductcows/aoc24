import re

from utils import get_lines, get_input_for_day, runtime


@runtime
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
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d1')))
