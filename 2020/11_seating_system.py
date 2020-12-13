from session import fetch

RAW_DATA = fetch(2020, 11)

result_part_1 = 0
result_part_2 = 0


def parse_data(data):
    return [[x for x in line] for line in data.splitlines()]


def check_surround(state, x, y, type_):
    occupied = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            try:
                k = x + i
                l = y + j
                if k < 0 or l < 0:
                    continue
                if state[k][l] == '#':
                    occupied += 1
            except IndexError:
                pass
    if type_ == 'L' and occupied == 0:
        return True
    if type_ == '#' and occupied >= 4:
        return True
    return False


def run_round(data):
    input_ = parse_data(data)
    output = parse_data(data)
    for x in range(len(input_)):
        for y in range(len(input_[0])):
            if input_[x][y] == '.':
                continue
            switch = check_surround(input_, x, y, input_[x][y])
            if switch:
                output[x][y] = 'L' if input_[x][y] == '#' else '#'
    result = []
    for line in output:
        result.append(''.join(line))
    return '\n'.join(result)

old = RAW_DATA
count = 0
while True:
    count += 1
    new = run_round(old)
    if new == old:
        break
    old = new

result_part_1 = len([x for x in new if x == '#'])


DIRECTION = {
    0: [-1, -1],
    1: [-1, 0],
    2: [-1, 1],
    3: [0, -1],
    4: [0, 1],
    5: [1, -1],
    6: [1, 0],
    7: [1, 1]
}

def check_surround(state, x, y, type_):
    occupied = 0
    for i in range(8):
        seat_found = False
        k = x
        l = y
        while not seat_found:
            k = k + DIRECTION[i][0]
            l = l + DIRECTION[i][1]
            try:
                if k < 0 or l < 0 or state[k][l] == 'L':
                    seat_found = True
                    continue
                if state[k][l] == '#':
                    occupied += 1
                    seat_found = True
            except IndexError:
                seat_found = True
    if type_ == 'L' and occupied == 0:
        return True
    if type_ == '#' and occupied >= 5:
        return True
    return False


old = RAW_DATA
count = 0
while True:
    count += 1
    new = run_round(old)
    if new == old:
        break
    old = new

result_part_2 = len([x for x in new if x == '#'])



print(f"Part I:  {result_part_1}")
print(f"Part II: {result_part_2}")
