from functools import cache

from utils import get_lines, get_input_for_day, runtime


def digits(n):
    res, comp = 1, 10
    while n >= comp:
        res += 1
        comp *= 10
    return res


def bifurcate(n):
    power = 10 ** (digits(n) // 2)
    return n // power, n % power


@cache
def stones(num, repetitions):
    if repetitions == 0:
        return 1
    if num == 0:
        return stones(1, repetitions - 1)

    dig = digits(num)
    if dig % 2 == 0:
        l, r = bifurcate(num)
        return stones(l, repetitions - 1) + stones(r, repetitions - 1)

    return stones(num * 2024, repetitions - 1)


@runtime
def run(lines):
    seeds = [int(num) for num in lines[0].split(' ')]
    repetitions = 25

    total = 0
    for seed in seeds:
        total += stones(seed, repetitions)

    return total


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d11')))
