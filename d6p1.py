from utils import get_lines, get_input_for_day, runtime


def first_index(l, pred):
    for i, e in enumerate(l):
        if pred(e):
            return i
    return -1


def run_simulation(grid, start_row, start_col, row_step=-1, col_step=0, **kwargs):
    seen = kwargs.get('seen', set())
    row, col, m, n = start_row, start_col, len(grid), len(grid[0])

    while True:
        while True:
            seen.add((row, col))
            next_row, next_col = row + row_step, col + col_step
            if next_row < 0 or next_col < 0 or next_row >= m or next_col >= n:
                return
            if grid[next_row][next_col] == '#':
                break

            row, col = next_row, next_col

        row_step, col_step = col_step, -row_step


@runtime
def run(lines):
    grid = lines
    start_row = first_index(grid, lambda s: '^' in s)
    start_col = first_index(grid[start_row], lambda c: c == '^')

    all_visited = set()
    run_simulation(grid, start_row, start_col, seen=all_visited)

    return len(all_visited)


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d6')))
