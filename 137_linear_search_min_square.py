import sys


def main():
    k = int(input())
    coords = [tuple(map(int, line.split())) for line in sys.stdin.readlines()]

    min_x = -1
    min_y = -1
    max_x = -1
    max_y = -1

    for coord in coords:
        x, y = coord
        if min_x == -1:
            min_x = x
        if min_y == -1:
            min_y = y
        if max_x == -1:
            max_x = x
        if max_y == -1:
            max_y = y
        if min_x > x:
            min_x = x
        if min_y > y:
            min_y = y
        if max_x < x:
            max_x = x
        if max_y < y:
            max_y = y

    print(min_x, min_y, max_x, max_y)


if __name__ == '__main__':
    main()