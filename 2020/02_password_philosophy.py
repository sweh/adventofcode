from session import fetch

RAW_DATA = fetch('https://adventofcode.com/2020/day/2/input')

result_part_1 = 0
result_part_2 = 0
for line in RAW_DATA.splitlines():
    rule, password = line.split(': ')
    amount, letter = rule.split()
    min_, max_ = amount.split('-')
    min_ = int(min_)
    max_ = int(max_)

    if min_ <= password.count(letter) <= max_:
        result_part_1 += 1

    first = password[min_-1] == letter
    second = password[max_-1] == letter
    if (first and not second) or (not first and second):
        result_part_2 += 1

print(f'Part I:  {result_part_1}')
print(f'Part II: {result_part_2}')
