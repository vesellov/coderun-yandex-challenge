import sys


def main():    
    n = int(input())
    matrix = list(map(lambda line: tuple(map(int, line.split())), sys.stdin.readlines()))
    begin, end = map(int, matrix.pop(-1))
    
    if begin == end:
        print(0)
        return

    graph = {i: set() for i in range(1, n + 1)}

    for y in range(n):
        for x in range(n):
            if matrix[y][x]:
                graph[y+1].add(x+1)

    visited = []

    queue = []
    queue.append([begin, ])

    while queue:
        current_path = queue.pop(0)
        current_node = current_path[-1]
        
        if current_node not in visited:

            for i in graph[current_node]:

                new_path = list(current_path)
                new_path.append(i)
                queue.append(new_path)

                if i == end:
                    print(len(new_path) - 1)
                    print(' '.join(map(str, new_path)))
                    return

            visited.append(current_node)

    print(-1)

if __name__ == '__main__':
    main()
