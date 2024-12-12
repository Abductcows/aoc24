from collections import deque

from utils import get_lines, get_input_for_day, runtime


def get_neighbors(row, col, m, n):
    base = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
    return [e for e in base if 0 <= e[0] < m and 0 <= e[1] < n]


def get_trailhead_count(grid, row, col):
    m, n = len(grid), len(grid[0])
    seen = {(row, col)}
    to_process = deque([(row, col)])

    trailhead_count = 0
    while to_process:
        row, col = to_process.pop()
        val = grid[row][col]

        if val == 9:
            trailhead_count += 1
            continue

        for neighbor in get_neighbors(row, col, m, n):
            if grid[neighbor[0]][neighbor[1]] == val + 1 and neighbor not in seen:
                seen.add(neighbor)
                to_process.appendleft(neighbor)

    return trailhead_count


@runtime
def run(lines):
    grid = [[int(digit) for digit in line] for line in lines]
    trail_starts = [(row, col) for row in range(len(grid)) for col in range(len(grid[0])) if grid[row][col] == 0]

    total = 0
    for start in trail_starts:
        total += get_trailhead_count(grid, *start)

    return total


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d10')))
