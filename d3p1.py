import re
from functools import reduce

from utils import get_lines, get_input_for_day


def run(lines):
    ans = 0

    for line in lines:
        muls = re.findall(r'mul\(\d+,\d+\)', line)
        for mul in muls:
            ans += reduce(lambda acc, v: acc * v, map(int, re.findall(r'\d+', mul)), 1)

    return ans

if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d3')))
