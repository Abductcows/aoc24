from utils import get_lines, get_input_for_day, runtime


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


@runtime
def run(lines):
    letters = lines
    m, n = len(letters), len(letters[0])

    query = 'MAS'
    middle = query[len(query) // 2]
    q1, q2 = [query[:len(query) // 2], query[::-1][:len(query) // 2]]

    total = 0
    for row in range(m):
        for col in range(n):
            if letters[row][col] != middle:
                continue

            found = 0
            for row_step, col_step in [(1, 1), (1, -1)]:  # main, secondary diagonals
                if (look_for(q1, letters, row + row_step, col + col_step, row_step, col_step) and
                        look_for(q2, letters, row - row_step, col - col_step, -row_step, -col_step) or
                        # reversed search
                        look_for(q2, letters, row + row_step, col + col_step, row_step, col_step) and
                        look_for(q1, letters, row - row_step, col - col_step, -row_step, -col_step)):
                    found += 1
            if found == 2:  # both diagonals simultaneously
                total += 1

    return total


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d4')))
