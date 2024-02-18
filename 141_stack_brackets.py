import sys


def main():
    try:
        inp = input().strip()
    except:
        inp = ''

    if not inp:
        print('yes')
        return

    stack = []

    for v in inp:

        if not v or v == ' ':
            continue

        if v in ['(', '{', '[', ]:
            stack.append(v)

        else:

            if not stack:
                print('no')
                return

            stack_last = stack[-1]

            if v == ')':
                if stack_last != '(':
                    print('no')
                    return
                stack.pop()

            elif v == ']':
                if stack_last != '[':
                    print('no')
                    return
                stack.pop()

            elif v == '}':
                if stack_last != '{':
                    print('no')
                    return
                stack.pop()

    if not stack:
        print('yes')
    else:
        print('no')


if __name__ == '__main__':
    main()