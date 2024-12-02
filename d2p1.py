def get_lines(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip('\n'))

    while lines and not lines[-1]:
        lines.pop()

    return lines


def is_safe_sequence(nums):
    increasing = nums[0] < nums[1]

    for i in range(len(nums) - 1):
        test1 = nums[i] == nums[i + 1]
        test2 = nums[i + 1] > nums[i] and not increasing
        test3 = nums[i + 1] < nums[i] and increasing
        test4 = nums[i + 1] > nums[i] + 3 and increasing
        test5 = nums[i + 1] + 3 < nums[i] and not increasing

        if test1 or test2 or test3 or test4 or test5:
            return False

    return True


def run(filename):
    lines = get_lines(filename)

    total_safe = 0

    for line in lines:
        nums = [int(e) for e in line.split(' ')]

        if is_safe_sequence(nums):
            total_safe += 1

    print(total_safe)


if __name__ == '__main__':
    run('example.txt')
    run('input.txt')
