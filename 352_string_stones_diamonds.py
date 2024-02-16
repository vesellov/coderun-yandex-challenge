import sys


def main():
    j = input()
    s = input()

    diamonds = set(j)

    total = 0

    for c in s:
        if c in diamonds:
            total += 1

    print(total)


if __name__ == '__main__':
    main()