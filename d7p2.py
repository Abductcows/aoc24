import itertools
import re

from utils import get_lines, get_input_for_day

from itertools import product


def pad_for(n):
    pad = 10
    while n >= pad:
        pad *= 10
    return pad


def run(lines):
    total = 0

    for line in lines:
        values = re.findall(r'\d+', line)
        result, operands = int(values[0]), list(map(int, values[1:]))

        op_arrangements = itertools.product(('*', '+', '||'), repeat=len(operands) - 1)

        for arrangement in op_arrangements:
            acc = operands[0]

            for i in range(len(arrangement)):
                if arrangement[i] == '+':
                    acc += operands[i + 1]
                elif arrangement[i] == '*':
                    acc *= operands[i + 1]
                else:
                    acc = acc * pad_for(operands[i + 1]) + operands[i + 1]

            if acc == result:
                total += result
                break

    return total


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d7')))
