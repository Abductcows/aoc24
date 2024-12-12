import itertools
import re

from utils import get_lines, get_input_for_day, runtime


@runtime
def run(lines):
    total = 0

    for line in lines:
        values = re.findall(r'\d+', line)
        result, operands = int(values[0]), list(map(int, values[1:]))
        op_arrangements = itertools.product('+*', repeat=len(operands) - 1)

        for arrangement in op_arrangements:
            acc = operands[0]

            for i in range(len(arrangement)):
                if arrangement[i] == '+':
                    acc += operands[i + 1]
                else:
                    acc *= operands[i + 1]

            if acc == result:
                total += result
                break

    return total


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d7')))
