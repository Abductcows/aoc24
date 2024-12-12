from utils import get_lines, get_input_for_day, runtime


def sum_elements_with_multiplier(count, multiplier, file_id):
    summed = count * (2 * multiplier + count - 1) // 2 * file_id
    return summed, multiplier + count


@runtime
def run(lines):
    data = list(map(int, lines[0]))
    n = len(data)
    assert n % 2 == 1

    l, r = -1, n + 1

    total = 0
    multiplier = 0
    file_id = n // 2 + 1
    spaces_available, to_consume = 0, 0

    while True:
        if spaces_available == 0:
            l += 2
            if l >= r:
                break
            cur_sum, multiplier = sum_elements_with_multiplier(data[l - 1], multiplier, l // 2)
            total += cur_sum
            spaces_available = data[l]
        if to_consume == 0:
            r -= 2
            file_id -= 1
            if l >= r:
                break
            to_consume = data[r]

        actual = min(spaces_available, to_consume)
        if actual:
            cur_sum, multiplier = sum_elements_with_multiplier(actual, multiplier, file_id)
            total += cur_sum

        spaces_available -= actual
        to_consume -= actual

    if to_consume > 0:
        cur_sum, multiplier = sum_elements_with_multiplier(to_consume, multiplier, file_id)
        total += cur_sum

    return total


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d9')))
