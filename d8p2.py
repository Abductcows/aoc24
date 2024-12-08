from collections import defaultdict
from itertools import product

from utils import get_lines, get_input_for_day


def get_antinodes(antennas, type, m, n):
    antennas = antennas[type]

    antinodes = []
    for i in range(len(antennas) - 1):
        for j in range(i + 1, len(antennas)):
            an1, an2 = antennas[i], antennas[j]
            rowdiff, coldiff = an1[0] - an2[0], an1[1] - an2[1]

            for row, col, step_sign in ((*an1, 1), (*an2, -1)):
                while 0 <= row < m and 0 <= col < n:
                    antinodes.append((row, col))
                    row += step_sign * rowdiff
                    col += step_sign * coldiff

    return antinodes


def run(lines):
    grid = lines
    m, n = len(grid), len(grid[0])

    antennas = defaultdict(list)
    for row, col in product(range(m), range(n)):
        if grid[row][col] == '.':
            continue
        antennas[grid[row][col]].append((row, col))

    antinodes = set()
    for antenna_type in antennas:
        antinodes.update(get_antinodes(antennas, antenna_type, m, n))

    return len(antinodes)


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d8')))
