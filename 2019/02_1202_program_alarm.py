from session import fetch

RAW_DATA = fetch(2019, 2)

result_part_1 = 0
result_part_2 = 0

PROG = [int(i) for i in RAW_DATA.split(',')]
PROG[1] = 12
PROG[2] = 2


def run():
    i = 0
    while PROG[i] != 99:
        command = PROG[i]
        if command == 1:
            PROG[PROG[i+3]] = PROG[PROG[i+1]] + PROG[PROG[i+2]]
        elif command == 2:
            PROG[PROG[i+3]] = PROG[PROG[i+1]] * PROG[PROG[i+2]]
        else:
            raise ValueError(f'Something went wrong. Opcode {command} found')
        i += 4

run()

result_part_1 = PROG[0]

for i in range(99):
    for j in range(99):
        PROG = [int(i) for i in RAW_DATA.split(',')]
        PROG[1] = i
        PROG[2] = j
        run()
        if PROG[0] == 19690720:
            result_part_2 = 100 * i + j


print(f"Part I:  {result_part_1}")
print(f"Part II: {result_part_2}")
