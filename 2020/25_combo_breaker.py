from session import fetch

RAW_DATA = fetch(2020, 25)
import itertools


def part1(s):
    a, b = map(int, s.splitlines())

    cracking_val = 1
    mod = 20201227
    for exp in itertools.count():
        if cracking_val == a:
            base = b
            break
        if cracking_val == b:
            base = a
            break
        cracking_val = (cracking_val * 7) % mod

    answer = pow(base, exp, mod)
    print(f'The answer to part one is {answer}')

def part2(s):
    print('There is no part two for Christmas!')

part1(RAW_DATA)
part2(RAW_DATA)
