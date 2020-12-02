from session import fetch

RAW_DATA = fetch('https://adventofcode.com/2020/day/1/input')

INPUT = [int(i) for i in RAW_DATA.splitlines()]

found = False
for i in INPUT:
    if found:
        break
    for j in INPUT:
        if found:
            break
        if i + j == 2020:
            found = True
            print(f'PART I: {i * j}')

found = False
for i in INPUT:
    if found:
        break
    for j in INPUT:
        if found:
            break
        for k in INPUT:
            if found:
                break
            if i + j + k == 2020:
                found = True
                print(f'PART II: {i * j * k}')
