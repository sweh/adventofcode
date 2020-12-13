from session import fetch

RAW_DATA = fetch(2020, 5)

result_part_1 = 0
result_part_2 = 0


def parse(binput, rows, lower_char):
    for char in binput[:-1]:
        if char == lower_char:
            rows[1] = int((rows[1] - rows[0])/2+rows[0])
        else:
            rows[0] = round(rows[1]-(rows[1]-rows[0])/2)
    if binput[-1] == lower_char:
        return rows[0]
    return rows[1]


def seat_number(binput):
    row = parse(binput[:7], [0, 127], 'F')
    column = parse(binput[7:], [0, 7], 'L')
    return row * 8 + column


snbs = []

for binput in RAW_DATA.splitlines():
    snb = seat_number(binput)
    if snb > result_part_1:
        result_part_1 = snb
    snbs.append(snb)

snbs = sorted(snbs)


for i, seat in enumerate(snbs):
    if i == 0:
        continue
    if seat - snbs[i-1] == 2:
        result_part_2 = seat -1


print(f"Part I:  {result_part_1}")
print(f"Part II: {result_part_2}")
