from session import fetch

RAW_DATA = fetch(2019, 1)

INPUT = [int(i) for i in RAW_DATA.splitlines()]

result_part_1 = 0
result_part_2 = 0


def calc_fuel(mass, first=False):
    fuel = int(mass/3)-2
    if first:
        mass = 0
    if fuel <= 0:
        return mass
    return mass + calc_fuel(fuel)


for i in INPUT:
    result_part_1 += int(i/3)-2
    result_part_2 += calc_fuel(i, True)


print(f"Part I:  {result_part_1}")
print(f"Part II: {result_part_2}")
