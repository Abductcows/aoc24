from collections import defaultdict
from itertools import product

from utils import get_lines, get_input_for_day


def get_antinodes(antennas, type):
    antennas = antennas[type]

    antinodes = []
    for i in range(len(antennas) - 1):
        for j in range(i + 1, len(antennas)):
            an1, an2 = antennas[i], antennas[j]

            rowdiff, coldiff = an1[0] - an2[0], an1[1] - an2[1]
            antinodes.append((an1[0] + rowdiff, an1[1] + coldiff))
            antinodes.append((an2[0] - rowdiff, an2[1] - coldiff))

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
        for antinode in get_antinodes(antennas, antenna_type):
            if 0 <= antinode[0] < m and 0 <= antinode[1] < n:
                antinodes.add(antinode)

    return len(antinodes)


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d8')))
