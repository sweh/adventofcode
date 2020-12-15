from session import fetch

RAW_DATA = fetch(2020, 14)

result_part_1 = 0
result_part_2 = 0

MASK = 'X' * 36
DATA = {}


for line in RAW_DATA.splitlines():
    if line.startswith('mask'):
        MASK = line.split(' = ')[1]
    else:
        addr, value = line.split(' = ')
        addr = int(addr.split('[')[1][:-1])
        value = int(value)
        value = str(bin(value)).split('0b', 1)[1].strip()
        value = "{:036d}".format(int(value))
        for i in range(len(MASK)):
            if MASK[i] != 'X':
                value = list(value)
                value[i] = MASK[i]
                value = ''.join(value)
        value = int(value, 2)
        DATA[addr] = value


result_part_1 = sum(DATA.values())
print(f"Part I:  {result_part_1}")

MASK = '0' * 36
DATA = {}

def get_floating(addr):
    addr = list(addr)
    amount = pow(2, addr.count('X'))
    fmt = "{:0%sd}" % addr.count('X')
    for i in range(amount):
        result = addr[:]
        submask = fmt.format(int(str(bin(i)).split('0b', 1)[1].strip()))
        for j in submask:
            result[result.index('X')] = j
        yield ''.join(result)


for line in RAW_DATA.splitlines():
    if line.startswith('mask'):
        MASK = line.split(' = ')[1]
    else:
        addr, value = line.split(' = ')
        addr = int(addr.split('[')[1][:-1])
        value = int(value)

        addr = str(bin(addr)).split('0b', 1)[1].strip()
        addr = "{:036d}".format(int(addr))
        for i in range(len(MASK)):
            if MASK[i] != '0':
                addr = list(addr)
                addr[i] = MASK[i]
                addr = ''.join(addr)
        for addr in get_floating(addr):
            addr = int(addr, 2)
            DATA[addr] = value

result_part_2 = sum(DATA.values())

print(f"Part II: {result_part_2}")
