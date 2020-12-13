from session import fetch

RAW_DATA = fetch(2020, 9)

result_part_1 = 0
result_part_2 = 0

PREAMBLE = 25
INPUT = [int(i) for i in RAW_DATA.splitlines()]

for i, v in enumerate(INPUT[PREAMBLE:]):
    found = False
    for x in INPUT[i:PREAMBLE+i]:
        for y in INPUT[i:PREAMBLE+i]:
            if x + y == v:
                found = True
                break
        if found:
            break
    if not found:
        result_part_1 = v
        break

print(f"Part I:  {result_part_1}")

for i, v in enumerate(INPUT):
    sum_ = v
    j = i
    while sum_ < result_part_1:
        j += 1
        sum_ += INPUT[j]
    if sum_ == result_part_1:
        result_part_2 = min(INPUT[i:j+1]) + max(INPUT[i:j+1])
        break

print(f"Part II: {result_part_2}")
