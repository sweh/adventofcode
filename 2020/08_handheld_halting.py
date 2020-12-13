from session import fetch

RAW_DATA = fetch(2020, 8).splitlines()

result_part_1 = 0
result_part_2 = 0

ACCU = 0
LINE = 0
EXECUTED = {}


def execute(line, accu):
    command, arg = RAW_DATA[line].split()
    if command == 'nop':
        line += 1
        return (line, accu)
    number = int(arg[1:])
    if command == 'acc':
        line += 1
        if arg[0] == '+':
            accu += number
        else:
            accu -= number
        return (line, accu)
    if command == 'jmp':
        if arg[0] == '+':
            line += number
        else:
            line -= number
        return (line, accu)


while True:
    if LINE in EXECUTED:
        result_part_1 = ACCU
        break
    EXECUTED[LINE] = None
    LINE, ACCU = execute(LINE, ACCU)

print(f"Part I:  {result_part_1}")


for change_line in EXECUTED.copy():
    ACCU = 0
    LINE = 0
    EXECUTED = {}
    RAW_DATA = fetch(2020, 8).splitlines()

    command, arg = RAW_DATA[change_line].split()
    if command == 'acc':
        continue
    if command == 'nop':
        RAW_DATA[change_line] = f'jmp {arg}'
    elif command == 'jmp':
        RAW_DATA[change_line] = f'nop {arg}'

    terminated_correctly = True
    while True:
        if LINE in EXECUTED:
            terminated_correctly = False
            break
        if LINE >= len(RAW_DATA):
            break
        EXECUTED[LINE] = None
        LINE, ACCU = execute(LINE, ACCU)

    if terminated_correctly:
        result_part_2 = ACCU
        break


print(f"Part II: {result_part_2}")
