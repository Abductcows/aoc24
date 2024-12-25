from utils import get_lines, get_input_for_day, runtime

in_map = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}


def did_i_move(grid, row, col, row_step, col_step):
    nrow, ncol = row + row_step, col + col_step

    if grid[nrow][ncol] == 'O':
        status = did_i_move(grid, nrow, ncol, row_step, col_step)
        if not status:
            return False
    if grid[nrow][ncol] == '.':
        grid[nrow][ncol] = grid[row][col]
        grid[row][col] = '.'
        return True
    if grid[nrow][ncol] == '#':
        return False


def execute(grid, instruction, rrow, rcol):
    row_step, col_step = in_map[instruction]

    if did_i_move(grid, rrow, rcol, row_step, col_step):
        return rrow + row_step, rcol + col_step

    return rrow, rcol


@runtime
def run(lines):
    i = 0
    robot_row, robot_col = -1, -1

    grid = []
    while lines[i]:
        if robot_row < 0 <= (robot_col := lines[i].find('@')):
            robot_row = i

        grid.append(list(lines[i]))
        i += 1

    for line in lines[i + 1:]:
        for instruction in line:
            robot_row, robot_col = execute(grid, instruction, robot_row, robot_col)

    return calculate_score(grid)


def calculate_score(grid):
    m, n = len(grid), len(grid[0])
    total = 0

    for row in range(m):
        for col in range(n):
            if grid[row][col] == 'O':
                total += 100 * row + col

    return total


if __name__ == '__main__':
    print(run(get_input_for_day('d15')))
    # print(run(get_lines('example.txt')))
