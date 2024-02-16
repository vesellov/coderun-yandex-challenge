import sys


def main():
    weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', )
    days, weekday_start = sys.stdin.readline().split()
    days = int(days)

    row = 0
    col = weekdays.index(weekday_start)
    day = 0

    if col > 0:
        sys.stdout.write('.. ' * col)

    while day < days:
        day += 1
        col += 1

        if day < 10:
            sys.stdout.write('.%d' % day)
        else:
            sys.stdout.write('%d' % day)

        if col >= 7:
            col = 0
            row += 1
            sys.stdout.write('\n')
        else:
            sys.stdout.write(' ')

    if col > 0:
        sys.stdout.write('\n')


if __name__ == '__main__':
    main()
