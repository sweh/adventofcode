from session import fetch

RAW_DATA = fetch(2019, 3)

result_part_1 = 0
result_part_2 = 0


COORDS = {0: {}, 1: {}}


def follow(wire, stop_at=None):
    coord = [0, 0]
    steps = 0
    for p in RAW_DATA.splitlines()[wire].split(','):
        direction = p[0]
        length = int(p[1:])
        for i in range(length):
            steps += 1
            if direction == 'R':
                coord[1] += 1
            elif direction == 'L':
                coord[1] -= 1
            elif direction == 'U':
                coord[0] += 1
            else:
                coord[0] -= 1
            if stop_at and stop_at == tuple(coord):
                return steps
            COORDS[wire].setdefault(coord[0], [])
            COORDS[wire][coord[0]].append(coord[1])


for wire in [0, 1]:
    follow(wire)

CROSSED = []

for i in COORDS[0]:
    for j in COORDS[0][i]:
        if i in COORDS[1] and j in COORDS[1][i]:
            CROSSED.append((i, j))

for i, j in CROSSED:
    if i < 0:
        i = 0 - i
    if j < 0:
        j = 0 - j
    if not result_part_1 or i + j < result_part_1:
        result_part_1 = i + j

print(f"Part I:  {result_part_1}")

for coord in CROSSED:
    steps = follow(0, coord) + follow(1, coord)
    if not result_part_2 or steps < result_part_2:
        result_part_2 = steps

print(f"Part II: {result_part_2}")
