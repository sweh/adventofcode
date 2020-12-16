from session import fetch

RAW_DATA = fetch(2020, 16)

result_part_1 = 0
result_part_2 = 0

RULES, MY, NEARBY = RAW_DATA.split('\n\n')

VALID_NUMBERS = set()
NAMED_VALID_NUMBERS = dict()

VALID_TICKETS = []

for line in RULES.splitlines():
    name, rulestr = line.split(': ')
    for rule in rulestr.split(' or '):
        min_, max_ = rule.split('-')
        VALID_NUMBERS.update(range(int(min_), int(max_)+1))
        NAMED_VALID_NUMBERS.setdefault(name, set())
        NAMED_VALID_NUMBERS[name].update(range(int(min_), int(max_)+1))


for ticket in NEARBY.splitlines()[1:]:
    valid = True
    for num in ticket.split(','):
        num = int(num)
        if num not in VALID_NUMBERS:
            result_part_1 += num
            valid = False
    if valid:
        VALID_TICKETS.append([int(n) for n in ticket.split(',')])

VALID = dict()
INVALID = dict()

for ticket in VALID_TICKETS:
    for index, value in enumerate(ticket):
        for name, valid_numbers in NAMED_VALID_NUMBERS.items():
            if value in valid_numbers:
                if name not in INVALID.get(index, []):
                    VALID.setdefault(index, set())
                    VALID[index].add(name)
            else:
                if name in VALID.get(index, []):
                    VALID[index].remove(name)
                INVALID.setdefault(index, set())
                INVALID[index].add(name)

# Remove duplicates
for _ in range(100):
    for index, names in VALID.items():
        if len(names) == 1:
            toremove = list(names)[0]
            for subindex in VALID:
                if subindex == index or toremove not in VALID[subindex]:
                    continue
                VALID[subindex].remove(toremove)

MY_TICKET = [int(n) for n in MY.splitlines()[1].split(',')]

for index, names in VALID.items():
    name = list(names)[0]
    if name.startswith('departure'):
        if not result_part_2:
            result_part_2 = MY_TICKET[index]
        else:
            result_part_2 *= MY_TICKET[index]

print(f"Part I:  {result_part_1}")
print(f"Part II: {result_part_2}")
