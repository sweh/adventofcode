from session import fetch

RAW_DATA = fetch(2020, 24)

import collections
import re


def get_initially_active_tiles(move_list):
    active_tiles = set()
    for moves in move_list.splitlines():
        x, y = 0, 0
        for move in re.findall('e|w|se|sw|nw|ne', moves):
            x, y = {
                'e': (x+1, y),
                'w': (x-1, y),
                'sw': (x-1, y-1),
                'se': (x, y-1),
                'nw': (x, y+1),
                'ne': (x+1, y+1)
                }[move]
        pos = (x, y)
        if pos in active_tiles:
            active_tiles.remove(pos)
        else:
            active_tiles.add(pos)
    return active_tiles

def part1(s):
    answer = len(get_initially_active_tiles(s))
    print(f'The answer to part one is {answer}')

def all_neighbors(x, y):
    return [(x+1, y),
            (x-1, y),
            (x-1, y-1),
            (x, y-1),
            (x, y+1),
            (x+1, y+1)]

def iterate(active_tiles):
    neighbor_counts = collections.defaultdict(int)
    for pos in active_tiles:
        for n in all_neighbors(*pos):
            neighbor_counts[n] += 1
    new_active = {pos
                  for pos in active_tiles
                  if neighbor_counts.pop(pos, 0) in (1, 2)}
    new_active |= {pos
                   for pos, count in neighbor_counts.items()
                   if count == 2}
    return new_active

def part2(s):
    active_tiles = get_initially_active_tiles(s)
    for _ in range(100):
        active_tiles = iterate(active_tiles)
    answer = len(active_tiles)
    print(f'The answer to part one is {answer}')

part1(RAW_DATA)
part2(RAW_DATA)
