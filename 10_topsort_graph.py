import sys


def main():
    n, m = map(int, input().split())
    routes_list = list(map(lambda line: tuple(map(int, line.split())), sys.stdin.readlines()))

    graph = {i: [] for i in range(1, n + 1)}

    for p1, p2 in routes_list:
        graph[p1].append(p2)

    weight = {i: 0 for i in range(1, n + 1)}

    for p1 in graph.keys():
        for p2 in graph[p1]:
            weight[p2] += 1

    queue = []
    for i in range(1, n + 1):
        if weight[i] == 0:
            queue.append(i)

    visited_node = 0
    order = []

    while queue:
        u = queue.pop(0)
        order.append(u)

        for i in graph[u]:
            weight[i] -= 1

            if weight[i] == 0:
                queue.append(i)

        visited_node += 1

    if visited_node != n:
        print(-1)
    else:
        print(' '.join(map(str, order)))


if __name__ == '__main__':
    main()
