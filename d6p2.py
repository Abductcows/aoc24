from utils import get_lines, get_input_for_day, runtime


def first_index(l, pred):
    for i, e in enumerate(l):
        if pred(e):
            return i
    return -1


def encode(row, col, row_step, col_step):
    return (row << 18) | (col << 4) | ((row_step + 1) << 2) | (col_step + 1)


def decode(i):
    return (i >> 18) & 0x3FFF, (i >> 4) & 0x3FFF, ((i >> 2) & 0x3) - 1, (i & 0x3) - 1


def encode_pos_only(row, col):
    return (row << 18) | (col << 4)


def decode_pos_only(i):
    return (i >> 18) & 0x3FFF, (i >> 4) & 0x3FFF


def run_simulation(grid, start_row, start_col, row_step=-1, col_step=0, **kwargs):
    seen = kwargs.get('seen', set())
    first_prev = kwargs.get('prev', None)
    row, col, m, n = start_row, start_col, len(grid), len(grid[0])

    while True:
        state = encode(row, col, row_step, col_step)
        if state in seen:
            return True

        while True:
            seen.add(state)
            next_row, next_col = row + row_step, col + col_step
            if next_row < 0 or next_col < 0 or next_row >= m or next_col >= n:
                return False
            if grid[next_row][next_col] == '#':
                break

            if first_prev is not None:
                pos_only = encode_pos_only(next_row, next_col)
                if pos_only not in first_prev:
                    first_prev[pos_only] = state

            row, col = next_row, next_col

        row_step, col_step = col_step, -row_step


@runtime
def run(lines):
    grid = list(map(list, lines))
    start_row = first_index(grid, lambda s: '^' in s)
    start_col = first_index(grid[start_row], lambda c: c == '^')

    prev = dict()
    run_simulation(grid, start_row, start_col, prev=prev)

    total = 0
    for k in prev:
        row, col = decode_pos_only(k)
        grid[row][col] = '#'
        if run_simulation(grid, *decode(prev[k])):
            total += 1
        grid[row][col] = '.'

    return total


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d6')))
