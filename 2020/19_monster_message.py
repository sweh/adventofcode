from session import fetch
import itertools

RAW_DATA = fetch(2020, 19)

result_part_1 = 0
result_part_2 = 0

RAW_RULES, RAW_DATA = RAW_DATA.split('\n\n')

RULES = {}

for rule in RAW_RULES.splitlines():
    i, rules = rule.split(': ')
    i = int(i)
    RULES.setdefault(i, [])
    for subrules_ in rules.split(' | '):
        subrule_ = []
        for rule in subrules_.split(' '):
            subrule_.append(eval(rule))
        RULES[i].append(subrule_)


def check_rule(rules, message, char):
    for subrule in rules:
        if isinstance(subrule, str):
            assert message[char] == subrule
            char += 1
        else:
            char = check(message, subrule, char)
    return char


def check(message, index=0, char=0):
    rules = RULES[index]
    valid = False
    for subrules in rules:
        if valid:
            continue
        try:
            char = check_rule(subrules, message, char)
        except AssertionError:
            pass
        else:
            valid = True
    if valid:
        if index == 0 and len(message) != char:
            raise AssertionError('Not valid')
        return char
    raise AssertionError('Not valid')


for msg in RAW_DATA.splitlines():
    try:
        check(msg)
    except:
        pass
    else:
        result_part_1 += 1

RULES[8] = [[42], [42, 8]]
RULES[11] = [[42, 31], [42, 11, 31]]


for msg in RAW_DATA.splitlines():
    try:
        check(msg)
    except:
        pass
    else:
        result_part_2 += 1


print(f"Part I:  {result_part_1}")
print(f"Part II: {result_part_2}")
