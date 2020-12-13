from session import fetch

RAW_DATA = fetch(2020, 13)

result_part_1 = 0
result_part_2 = 0


START = int(RAW_DATA.splitlines()[0])
BUSSES = [int(b) for b in RAW_DATA.splitlines()[1].split(',') if b != 'x']

TIME = START
while result_part_1 == 0:
    for bus in BUSSES:
        if TIME % bus == 0:
            result_part_1 = (TIME - START) * bus
    TIME += 1

print(f"Part I:  {result_part_1}")

BUSSES = [b for b in RAW_DATA.splitlines()[1].split(',')]


from functools import reduce


# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


n = []
a = []

for delay, part in enumerate(BUSSES):
    if part == 'x':
        continue
    n.append(int(part))
    a.append(int(part) - delay)

result_part_2 = chinese_remainder(n, a)

print(f"Part II: {result_part_2}")
