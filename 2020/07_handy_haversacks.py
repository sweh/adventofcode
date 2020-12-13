from session import fetch

RAW_DATA = fetch(2020, 7)

result_part_1 = 0
result_part_2 = 0

BAGS_PART_1 = {}
BAGS_PART_2 = {}

for line in RAW_DATA.splitlines():
    outer, inners = line.split(' bags contain ')
    for inner in inners.split(', '):
        if inner == 'no other bags.':
            continue
        inner = inner.split('bag')[0].strip()
        amount, inner = inner.split(' ', 1)
        BAGS_PART_1.setdefault(inner, [])
        BAGS_PART_1[inner].append(outer)
        BAGS_PART_2.setdefault(outer, [])
        BAGS_PART_2[outer].append((amount, inner))


shiny_gold_bags = []

def contains(bag):
    if bag not in BAGS_PART_1:
        return
    for inner in BAGS_PART_1[bag]:
        shiny_gold_bags.append(inner)
        contains(inner)

contains('shiny gold')
result_part_1 = len(set(shiny_gold_bags))


def contains(bag, bags=0):
    if bag not in BAGS_PART_2:
        return bags
    for amount, inner in BAGS_PART_2[bag]:
        amount = int(amount)
        bags += amount + (amount * contains(inner))
    return bags

result_part_2 = contains('shiny gold')

print(f"Part I:  {result_part_1}")
print(f"Part II: {result_part_2}")
