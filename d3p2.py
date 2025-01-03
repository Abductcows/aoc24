import re
from functools import reduce

from utils import get_lines, get_input_for_day, runtime


@runtime
def run(lines):
    ans = 0
    do_mul = True
    for line in lines:
        mult_pattern = r'mul\(\d+,\d+\)'
        do_pattern = r"do(?:n't)?\(\)"
        instructions = re.findall(f'{mult_pattern}|{do_pattern}', line)

        for instruction in instructions:
            if instruction.startswith('mul') and do_mul:
                ans += reduce(lambda acc, v: acc * v, map(int, re.findall(r'\d+', instruction)), 1)
            elif instruction.startswith('do'):
                do_mul = "n't" not in instruction

    return ans


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d3')))
