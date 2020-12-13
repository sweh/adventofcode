from session import fetch

RAW_DATA = fetch(2020, 12)

result_part_1 = 0
result_part_2 = 0

INPUT = [(l[0], int(l[1:])) for l in RAW_DATA.splitlines()]

POSITION = [0, 0]
FACE = 90

DIRECTIONS = {
    90: 'E',
    180: 'S',
    270: 'W',
    0: 'N',
    360: 'N'
}

def move(direction, amount):
    if direction == 'N':
        POSITION[1] -= amount
    elif direction == 'E':
        POSITION[0] += amount
    elif direction == 'S':
        POSITION[1] += amount
    elif direction == 'W':
        POSITION[0] -= amount


for direction, amount in INPUT:
    if direction in ('R', 'L'):
        assert amount in (0, 90, 180, 270, 360)
        for i in range(int(amount / 90)):
            if direction == 'R':
                if FACE == 360:
                    FACE = 90
                else:
                    FACE += 90
            else:
                if FACE == 0:
                    FACE = 270
                else:
                    FACE -= 90
    elif direction == 'F':
        move(DIRECTIONS[FACE], amount)
    else:
        move(direction, amount)

for pos in POSITION:
    if pos < 0:
        pos = 0 - pos
    result_part_1 += pos


print(f"Part I:  {result_part_1}")

WAYPOINT = [10, -1]
POSITION = [0, 0]

def move_waypoint(direction, amount):
    if direction == 'N':
        WAYPOINT[1] -= amount
    elif direction == 'E':
        WAYPOINT[0] += amount
    elif direction == 'S':
        WAYPOINT[1] += amount
    elif direction == 'W':
        WAYPOINT[0] -= amount


def move_ship(amount):
    for i in range(amount):
        POSITION[0] += WAYPOINT[0]
        POSITION[1] += WAYPOINT[1]


for direction, amount in INPUT:
    if direction in ('R', 'L'):
        assert amount in (0, 90, 180, 270, 360)
        for i in range(int(amount / 90)):
            x = WAYPOINT[0]
            y = WAYPOINT[1]
            if direction == 'R':
                WAYPOINT[0] = 0 - y
                WAYPOINT[1] = x
            else:
                WAYPOINT[0] = y
                WAYPOINT[1] = 0 - x
    elif direction == 'F':
        move_ship(amount)
    else:
        move_waypoint(direction, amount)

for pos in POSITION:
    if pos < 0:
        pos = 0 - pos
    result_part_2 += pos

print(f"Part II: {result_part_2}")
