import sys


def main():
    n = int(input())
    inp = list(map(int, input().split()))

    tupik = []
    out = []

    current_wagon = min(inp)

    while True:
        if not inp:
            break
        wagon = inp.pop(0)
        tupik.append(wagon)
        if current_wagon == wagon:
            break

    while inp:
        if not tupik:
            next_wagon = inp.pop(0)
            tupik.append(next_wagon)

        if tupik[-1] == current_wagon:
            top_wagon = tupik.pop(len(tupik) - 1)
            out.append(top_wagon)
            current_wagon += 1
            continue

        while True:
            if not inp:
                break
            next_wagon = inp.pop(0)
            tupik.append(next_wagon)
            if current_wagon == next_wagon:
                break

    while tupik:
        top_wagon = tupik.pop(len(tupik) - 1)
        if not out:
            out.append(top_wagon)
            continue
        if top_wagon == out[-1] + 1:
            out.append(top_wagon)
        else:
            print('NO')
            return

    print('YES')


if __name__ == '__main__':
    main()