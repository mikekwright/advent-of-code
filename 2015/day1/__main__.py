import os
import sys
import re


GOES_UP_PATTERN = r"\("
GOES_DOWN_PATTERN = r"\)"                      


def solve_day1_part2(santas_elevation_shifts: str) -> int:
    elevation = 0
    step = 1
    for change in santas_elevation_shifts:
        if change == '(':
            elevation += 1
        elif change == ')':
            elevation -= 1

        if elevation < 0:
            # We just entered the basement
            return step

        step += 1

    # We never entered the building
    return 0


def solve_day1(santas_elevation_shifts: str) -> int:
    return len(re.findall(GOES_UP_PATTERN, santas_elevation_shifts)) - len(re.findall(GOES_DOWN_PATTERN, santas_elevation_shifts))


def run_tests():
    def run_a_test(problem, *, input, expected, func=solve_day1):
        actual = func(input)
        print(f"'{problem}' pass" if actual == expected else f"'{problem}' FAIL {expected} != {actual}")

    run_a_test('floor 0', input='(())', expected=0)
    run_a_test('floor 0', input='()()', expected=0)
    run_a_test('floor 3', input='(((', expected=3)
    run_a_test('floor 3', input='(()(()(', expected=3)
    run_a_test('floor 3', input='))(((((', expected=3)
    run_a_test('floor -1', input='())', expected=-1)
    run_a_test('floor -1', input='))(', expected=-1)
    run_a_test('floor -3', input=')))', expected=-3)
    run_a_test('floor -3', input=')())())', expected=-3)


def test_filename(input_filename: str | None = None):
    run_tests()

    if input_filename is None:
        print('No filename provided, not testing the solution')
    elif not os.path.exists(input_filename):
        print('Unable to find the expected input file, please try again')
    else:
        with open(input_filename, 'r') as f:
            input = f.readline()
            print(f'Floors: {solve_day1(input)} and enters {solve_day1_part2(input)}')


if __name__ == '__main__':
    filename = None

    if len(sys.argv) > 1:
        filename = sys.argv[1]

    test_filename(filename)
