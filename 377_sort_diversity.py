import sys


def main():
    n = int(input())
    products = {}
    categories = set()
    category_products = {}
    for _ in range(n):
        product, category = map(int, input().split())
        products[product] = category
        categories.add(category)

    order = list(map(int, input().split()))

    if len(categories) == len(order):
        print(len(categories))
        return

    categories_indexes = {}

    for i in range(len(order)):
        product = order[i]
        category = products[product]
        if category not in categories_indexes:
            categories_indexes[category] = []
        categories_indexes[category].append(i)
        if category not in category_products:
            category_products[category] = []
        category_products[category].append(product)

    total_min = -1
    for category, category_indexes in categories_indexes.items():
        indexes = list(category_indexes)
        indexes.sort()
        min_diff = -1
        if len(indexes) == len(category_products[category]):
            min_diff = len(indexes)
        else:
            for i in range(len(indexes)-1):
                diff = abs(indexes[i+1] - indexes[i])
                if min_diff < 0:
                    min_diff = diff
                if min_diff > diff:
                    min_diff = diff
        if total_min < 0:
            total_min = min_diff
        if total_min > min_diff:
            total_min = min_diff

    print(total_min)

if __name__ == '__main__':
    main()