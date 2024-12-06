from collections import defaultdict

from utils import get_lines,get_input_for_day


def run(lines):
    befores = defaultdict(set)

    i = 0
    while '|' in lines[i]:
        nums = list(map(int, lines[i].split('|')))
        befores[nums[1]].add(nums[0])
        i += 1

    sum_of_middles = 0
    for line in lines[i + 1:]:
        nums = list(map(int, line.split(',')))
        right_order = True
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[j] in befores[nums[i]]:
                    right_order = False

        if right_order:
            sum_of_middles += nums[len(nums) // 2]

    return sum_of_middles


if __name__ == '__main__':
    print(run(get_lines('example.txt')))
    print(run(get_input_for_day('d5')))
