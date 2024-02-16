import sys


def main():
    n = int(input())
    inp = sys.stdin.readlines()
    walls = [[c == '*' for c in line.strip()] for line in inp[:-1]]
    x, y = inp[-1].split()
    x = int(x)
    y = int(y)

    directions = ((1, 0, ), (0, 1, ), (-1, 0, ), (0, -1, ), )

    visited = set()
    queue = []
    queue.append((x, y, ))

    while queue:
        point = queue.pop(0)

        if point not in visited:

            for direction in directions:
                next_point = (
                    point[0] + direction[0],
                    point[1] + direction[1],
                )
                if 1 <= next_point[0] <= n and 1 <= next_point[1] <= n:
                    if not walls[next_point[0]-1][next_point[1]-1]:
                        queue.append(next_point)

            visited.add(point)
        
    print(len(visited))

if __name__ == '__main__':
    main()