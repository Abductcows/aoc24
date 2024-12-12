import inspect
import re
import time
from pathlib import Path


def get_lines(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip('\n'))

    while lines and not lines[-1]:
        lines.pop()

    return lines


def get_input_for_day(day_with_num):
    assert re.fullmatch(r'd(\d+)', day_with_num)
    lines = []
    with open('inputs.txt') as file:
        while True:
            line = file.readline()
            if not line or line.startswith(f'{day_with_num}:'):
                break
        while True:
            line = file.readline()
            if not line or re.match(r'd(\d+):', line):
                break
            lines.append(line.rstrip('\n'))

    while lines and not lines[-1]:
        lines.pop()
    while lines and not lines[0]:
        lines.remove(0)

    return lines


def runtime(func):
    module_name = Path(inspect.getfile(func)).name[:-3]

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Runtime of {module_name}.{func.__name__}: {int(1_000 * (end_time - start_time)):_}ms")
        return result

    return wrapper
