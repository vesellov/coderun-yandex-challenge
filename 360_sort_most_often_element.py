import sys


def main():
    n = int(sys.stdin.readline())
    numbers = [int(i) for i in sys.stdin.readline().split()]
    assert len(numbers) == n

    counts = {}
    max_count = 0
    biggest_numbers = set()

    for num in numbers:
        if num not in counts:
            counts[num] = 0
        counts[num] += 1
        if counts[num] == max_count:
            biggest_numbers.add(num)
        elif counts[num] > max_count:
            max_count = counts[num]
            biggest_numbers.clear()
            biggest_numbers.add(num)

    print(max(biggest_numbers))

if __name__ == '__main__':
    main()
