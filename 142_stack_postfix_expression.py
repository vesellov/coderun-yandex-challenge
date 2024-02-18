import sys

sys.setrecursionlimit(150000)


def calc(inp, op):
    if len(inp) == 2:
        if op == '+':
            return int(inp[0]) + int(inp[1])
        elif op == '-':
            return int(inp[0]) - int(inp[1])
        elif op == '*':
            return int(inp[0]) * int(inp[1])
        elif op == '/':
            return int(inp[0]) / int(inp[1])

    if inp[2] in ['+', '-', '*', '/']:
        v1 = calc(inp[:2], inp[2])
        inp = inp[3:]
    else:
        v1 = inp[0]
        inp = inp[1:]

    if inp[-1] in ['+', '-', '*', '/']:
        v2 = calc(inp[:-1], inp[-1])
    else:
        v2 = inp[-1]

    if op == '+':
        return int(v1) + int(v2)
    elif op == '-':
        return int(v1) - int(v2)
    elif op == '*':
        return int(v1) * int(v2)
    elif op == '/':
        return int(v1) / int(v2)


def main1():
    inp = input().strip().split()
    print(calc(inp[:-1], inp[-1]))


def main2():
    inp = input().strip().split()

    stack = []
    for v in inp:
        if v.isdigit():
            stack.append(int(v))
            continue
        v2 = stack.pop()
        v1 = stack.pop()
        if v == '+':
            vv = v1 + v2
        elif v == '-':
            vv = v1 - v2
        elif v == '*':
            vv = v1 * v2
        stack.append(vv)

    print(stack[0])

if __name__ == '__main__':
    main2()
