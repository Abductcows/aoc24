from utils import run_with_file, get_input_for_day


def count_all_in_sequence(start, offsets, number_of_steps, letters, n):
    start_1d = n * start[0] + start[1]
    step = n * offsets[0] + offsets[1]
    stop = start_1d + step * number_of_steps
    x = letters[start_1d:stop:step]
    return x.count('XMAS') + ''.join(reversed(x)).count('XMAS')


def run(lines):
    n = len(lines)
    letters_1d = ''.join(lines)

    count = 0
    letter_traversals = [
        *[((row, 0), (0, 1), n) for row in range(n)],  # rows
        *[((0, col), (1, 0), n) for col in range(n)],  # cols

        ((0, 0), (1, 1), n),  # main diagonal
        ((0, n - 1), (1, -1), n),  # secondary diagonal

        *[((0, start_col), (1, 1), n - start_col) for start_col in range(1, n)],  # diagonals ltr above main
        *[((start_row, 0), (1, 1), n - start_row) for start_row in range(1, n)],  # diagonals ltr below main

        *[((0, start_col), (1, -1), start_col + 1) for start_col in range(0, n - 1)],  # diagonals rtl above secondary
        *[((start_row, n - 1), (1, -1), n - start_row) for start_row in range(1, n)]  # diagonals rtl below secondary
    ]

    for start, diffs, element_count in letter_traversals:
        count += count_all_in_sequence(start, diffs, element_count, letters_1d, n)
    return count


if __name__ == '__main__':
    print(run_with_file('example.txt', run))
    print(run(get_input_for_day('d4')))
