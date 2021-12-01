from session import fetch

RAW_DATA = fetch(2021, 1)

INPUT = [int(i) for i in RAW_DATA.splitlines()]

increases = 0
last = None
for v in INPUT:
    if not last:
        last = v
        continue
    if v > last:
        increases += 1
    last = v

print(f"PART I: {increases}")

increases = 0
last = None
for i, v in enumerate(INPUT):
    if not last:
        last = INPUT[i] + INPUT[i + 1] + INPUT[i + 2]
        continue
    try:
        INPUT[i + 2]
    except IndexError:
        continue
    current = INPUT[i] + INPUT[i + 1] + INPUT[i + 2]
    if current > last:
        increases += 1
    last = current

print(f"PART II: {increases}")
