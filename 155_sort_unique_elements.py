import sys


def main():
    n = int(input())
    data = list(map(int, input().split()))
    index = {}
    unique_elements = set()

    for value in data:
        if value not in index:
            index[value] = 0
        index[value] += 1
        if index[value] == 1:
            unique_elements.add(value)
        else:
            unique_elements.discard(value)
    
    print(len(unique_elements))


if __name__ == '__main__':
    main()
