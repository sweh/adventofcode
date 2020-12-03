from session import fetch

RAW_DATA = fetch("https://adventofcode.com/2020/day/3/input")

DATA = RAW_DATA.splitlines()

def fly(position, step_right, step_down):
    trees = 0
    while position[1] < len(DATA)-1:
        position[0] += step_right
        position[1] += step_down
        if position[0] >= len(DATA[0]):
            position[0] = position[0] - len(DATA[0])
        if DATA[position[1]][position[0]] == '#':
            trees += 1
    return trees


result_part_1 = fly([0, 0], 3, 1)

print(f"Part I:  {result_part_1}")

result_part_2 = (
    fly([0, 0], 1, 1) *
    fly([0, 0], 3, 1) *
    fly([0, 0], 5, 1) *
    fly([0, 0], 7, 1) *
    fly([0, 0], 1, 2)
)

print(f"Part II: {result_part_2}")
