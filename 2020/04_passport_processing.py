from session import fetch

RAW_DATA = fetch(2020 4)

result_part_1 = 0
result_part_2 = 0


def check_height(x):
    if x[-2:] == 'cm':
        return 150 <= int(x[0:3]) <= 193
    if x[-2:] == 'in':
        return 59 <= int(x[0:2]) <= 76
    raise ValueError(x)


def check_hair(x):
    assert len(x) == 7
    assert x[0] == '#'
    for char in x[1:]:
        assert char in [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            'a', 'b', 'c', 'd', 'e', 'f'
        ]
    return True


expected_keys = dict(
    byr=lambda x: len(x) == 4 and int(x) >= 1920 and int(x) <= 2002,
    iyr=lambda x: len(x) == 4 and int(x) >= 2010 and int(x) <= 2020,
    eyr=lambda x: len(x) == 4 and int(x) >= 2020 and int(x) <= 2030,
    hgt=check_height,
    hcl=check_hair,
    ecl=lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    pid=lambda x: len(x) == 9 and int(x),
)


for passport in RAW_DATA.split('\n\n'):
    data = {}
    valid_part_1 = valid_part_2 = True
    for line in passport.splitlines():
        for item in line.split():
            k, v = item.split(':')
            data[k] = v
    for key, check in expected_keys.items():
        if key not in data:
            valid_part_1 = False
            valid_part_2 = False
        if key in data and valid_part_2:
            try:
                valid_part_2 = check(data[key])
            except Exception:
                valid_part_2 = False

    if valid_part_1:
        result_part_1 += 1
    if valid_part_2:
        result_part_2 += 1

print(f"Part I:  {result_part_1}")
print(f"Part II: {result_part_2}")
