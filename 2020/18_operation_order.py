from session import fetch
import itertools

RAW_DATA = fetch(2020, 18)

result_part_1 = 0
result_part_2 = 0


def find_closing_index(subline):
    par = 0
    for index, char in enumerate(subline):
        if char == '(':
            par += 1
        elif char == ')' and par == 0:
            return index
        elif char == ')':
            par -= 1


def find_left_operand_index(subline):
    par = 0
    length = len(subline)
    for i in range(length):
        i = length - i - 1
        char = subline[i]
        if char == ')':
            par += 1
        elif char == '(':
            par -= 1
        if par == 0:
            return i


def find_right_operand_index(subline):
    par = 0
    length = len(subline)
    for i in range(length):
        char = subline[i]
        if char == '(':
            par += 1
        elif char == ')':
            par -= 1
        if par == 0:
            return i


def calc(line):
    pre = post = op = None
    index = 0
    while index < len(line):
        char = line[index]
        if char == '(':
            closing_index = find_closing_index(line[index+1:]) + index
            subresult = calc(line[index+1:closing_index+1])
            if pre is None:
                pre = subresult
            else:
                assert op is not None
                post = subresult
            index = closing_index + 1
        elif char in ('+', '*'):
            op = char
        elif char not in (' ', ')'):
            if pre is None:
                pre = int(char)
            else:
                post = int(char)
        if pre and op and post:
            pre = eval(f'{pre} {op} {post}')
            op = post = None
        index += 1
    return pre


def calc_pre(subline):
    if subline[-1] == ')':
        return subline[find_left_operand_index(subline):]
    else:
        return subline[-1]

def calc_post(subline):
    if subline[0] == '(':
        return subline[:find_right_operand_index(subline)+1]
    else:
        return subline[0]

def precedence_plus(line):
    line = line + ' '
    index = 0
    while index < len(line):
        if line[index] == '+':
            op = line[index]
            pre = calc_pre(line[:index-1])
            post = calc_post(line[index+2:])
            if line[index-2-len(pre)] != '(' or line[index+2+len(post)] != ')':  # noaq
                line = line.replace(
                    f'{pre} {op} {post}', f'({pre} {op} {post})'
                )
                index += 1
        index += 1
    return line



for line in RAW_DATA.splitlines():
    result_part_1 += calc(line)
    line = precedence_plus(line)
    result_part_2 += calc(line)

print(f"Part I:  {result_part_1}")
print(f"Part II: {result_part_2}")
