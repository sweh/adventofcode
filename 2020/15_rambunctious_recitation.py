from session import fetch

RAW_DATA = fetch(2020, 15)

result_part_1 = 0
result_part_2 = 0

INPUT = [int(i) for i in RAW_DATA.splitlines()[0].split(',')]
INDEX = dict()

for i, v in enumerate(INPUT):
    INDEX.setdefault(v, [])
    INDEX[v].append(i)

i = len(INPUT)

while i < 30000000:
    last_spoken = INPUT[i-1]
    if len(INDEX[last_spoken]) == 1:
        INPUT.append(0)
        INDEX.setdefault(0, [])
        INDEX[0].append(i)
    else:
        last_spoken_index = INDEX[last_spoken][-2] + 1
        INPUT.append(i - last_spoken_index)
        INDEX.setdefault(i - last_spoken_index, [])
        INDEX[i - last_spoken_index].append(i)
    i += 1

result_part_1 = INPUT[2019]
result_part_2 = INPUT[-1]

print(f"Part I:  {result_part_1}")
print(f"Part II: {result_part_2}")
