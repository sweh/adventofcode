from session import fetch
import itertools

RAW_DATA = fetch(2020, 17)

result_part_1 = 0
result_part_2 = 0


# Credits go to
#   https://www.reddit.com/r/adventofcode/comments/keqsfa/
#   2020_day_17_solutions/gg4cqow/
def run(data, dim, moves=6):
    for x in range(moves + 1):
        on = set((x, y, *(0,) * (dim - 2)) for x, y in itertools.product(range(len(data)), range(len(data[0]))) if data[y][x] == "#") if x==0 else {cube_pos for cube_pos in itertools.product(*[range([min(cube[di] for cube in on) for di in range(dim)][di] - 1, 2 + [max(cube[di] for cube in on) for di in range(dim)][di]) for di in range(dim)]) if len([neighbour_offset for neighbour_offset in set(itertools.product((-1, 0, 1), repeat=dim)) - {(0,) * dim} if tuple(map(sum, zip(cube_pos, neighbour_offset))) in on]) == 3 or cube_pos in on and len([neighbour_offset for neighbour_offset in set(itertools.product((-1, 0, 1), repeat=dim)) - {(0,) * dim} if tuple(map(sum, zip(cube_pos, neighbour_offset))) in on]) == 2}  # noqa
    return len(on)


result_part_1 = run(RAW_DATA.splitlines(), 3)

print(f"Part I:  {result_part_1}")

result_part_2 = run(RAW_DATA.splitlines(), 4)

print(f"Part II: {result_part_2}")
