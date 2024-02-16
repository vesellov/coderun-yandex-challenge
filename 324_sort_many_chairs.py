import sys


def main():
    n, m = map(int, input().split())
    sellers = list(map(int, input().split()))
    buyers = list(map(int, input().split()))

    sellers.sort()
    buyers.sort(reverse=True)

    total = 0

    shortes = min(len(sellers), len(buyers))

    for i in range(shortes):
        buyer = buyers[i]
        seller = sellers[i]
        if buyer > seller:
            total += buyer - seller

    print(total)


if __name__ == '__main__':
    main()