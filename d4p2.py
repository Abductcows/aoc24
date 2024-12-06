from itertools import product

from utils import get_lines, get_input_for_day


def run(lines):
    n = len(lines)

    letters = lines

    count = 0
    for row, col in product(range(n), repeat=2):
        c = letters[row][col]
        if c != 'A' or row == 0 or col == 0 or row == n - 1 or col == n - 1:
            continue

        main = letters[row - 1][col - 1] + letters[row + 1][col + 1]
        second = letters[row + 1][col - 1] + letters[row - 1][col + 1]
        if 'M' in main and 'M' in second and 'S' in main and 'S' in second:
            count += 1

    return count


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d4')))
