from session import fetch

RAW_DATA = fetch(2020, 10)

INPUT = sorted([int(i) for i in RAW_DATA.splitlines()])

result_part_1 = 0
result_part_2 = 0

JOINT_DIFFERENCES = {
    1: 0,
    3: 1  # The last connection to the device is always 3
}

left = 0

for right in INPUT:
    for i in [1, 3]:
        if right - left == i:
            JOINT_DIFFERENCES[i] += 1
    left = right

result_part_1 = JOINT_DIFFERENCES[1] * JOINT_DIFFERENCES[3]

print(f"Part I:  {result_part_1}")

INPUT.insert(0,0)
MAX = max(INPUT) + 3
INPUT.append(MAX);



# Credits go to:
# https://www.reddit.com/r/adventofcode/comments/ka9pc3/2020_day_10_part_2_suspicious_factorisation/gf9ipeh/

data = set(INPUT)
d = {i: 0 for i in range(6)}
p = max(data)
while p > 0:
    n = max({p-i for i in range(6)} - data)
    d[p-n] += 1
    p = n - 2

result_part_2 = 2**d[3] * 4**d[4] * 7**d[5]

print(f"Part II: {result_part_2}")
