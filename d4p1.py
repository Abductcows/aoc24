from utils import get_lines, get_input_for_day


def look_for(query, letters, row, col, row_step, col_step):
    traversed = []
    m, n = len(letters), len(letters[0])
    steps_left = len(query)
    while steps_left > 0 and 0 <= row < m and 0 <= col < n:
        traversed.append(letters[row][col])
        steps_left -= 1
        row += row_step
        col += col_step
    return ''.join(traversed) == query


def run(lines):
    letters = lines
    m, n = len(letters), len(letters[0])
    total = 0
    for row in range(m):
        for col in range(n):
            for row_step, col_step in [(0, 1), (1, 1), (1, 0), (1, -1)]:
                total += look_for('XMAS', letters, row, col, row_step, col_step)
                total += look_for('SAMX', letters, row, col, row_step, col_step)

    return total


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d4')))
