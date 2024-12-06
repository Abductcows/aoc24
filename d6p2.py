from utils import get_lines, get_input_for_day


def first_index(l, pred):
    for i, e in enumerate(l):
        if pred(e):
            return i
    return -1


def run_simulation(grid, start_row, start_col, row_step=-1, col_step=0, **kwargs):
    seen = kwargs.get('seen', set())
    row, col, m, n = start_row, start_col, len(grid), len(grid[0])
    while True:
        if (row, col, row_step, col_step) in seen:
            return True

        while True:
            seen.add((row, col, row_step, col_step))
            next_row, next_col = row + row_step, col + col_step
            if next_row < 0 or next_col < 0 or next_row >= m or next_col >= n:
                return False
            if grid[next_row][next_col] == '#':
                break

            row, col = next_row, next_col

        row_step, col_step = col_step, -row_step


def run(lines):
    grid = list(map(list, lines))
    start_row = first_index(grid, lambda s: '^' in s)
    start_col = first_index(grid[start_row], lambda c: c == '^')

    all_visited = set()
    run_simulation(grid, start_row, start_col, seen=all_visited)

    total = 0
    for entry in {(v[0], v[1]) for v in all_visited} - {(start_row, start_col)}:
        grid[entry[0]][entry[1]] = '#'
        if run_simulation(grid, start_row, start_col):
            total += 1
        grid[entry[0]][entry[1]] = '.'

    return total


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d6')))
