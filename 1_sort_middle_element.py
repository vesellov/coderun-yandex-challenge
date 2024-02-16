import sys


def main():
    l = list(map(int, sys.stdin.readline().split()))
    l.sort()
    print(l[1])


if __name__ == '__main__':
    main()
