from session import fetch

RAW_DATA = fetch(2020, 6)

result_part_1 = 0
result_part_2 = 0


for group in RAW_DATA.split('\n\n'):
    answers = []
    for line in group.splitlines():
        for answer in line:
            answers.append(answer)
    answers = set(answers)
    result_part_1 += len(answers)

print(f"Part I:  {result_part_1}")

for group in RAW_DATA.split('\n\n'):
    answers = [[c for c in group] for group in group.splitlines()]
    same_answers = set(answers[0])
    if answers[1:]:
        for answer in answers[1:]:
            same_answers = same_answers.intersection(set(answer))
    result_part_2 += len(same_answers)

print(f"Part II: {result_part_2}")

