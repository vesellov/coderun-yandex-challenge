import sys
import math


def main():
    n = int(input())

    coords = list(map(lambda line: tuple(map(int, line.split())), sys.stdin.readlines()))

    coords.insert(0, (0, 0, ))

    total = 0.0
    for i in range(len(coords) - 1):
        coord1 = coords[i]
        coord2 = coords[i+1]
        dx = coord2[0] - coord1[0]
        dy = coord2[1] - coord1[1]
        dl = math.sqrt(dx*dx + dy*dy)
        total += dl

    i = 0
    while i < len(coords) - 1:
        this_coord = coords[i]
        next_coord = coords[i+1]
        i += 1
        if this_coord[1] < next_coord[1]:
            continue
        starting_coord = this_coord
        while this_coord[1] >= next_coord[1] and i < len(coords) - 1:
            this_coord = coords[i]
            next_coord = coords[i+1]
            i += 1
        if starting_coord[1] < next_coord[1]:
            dx = starting_coord[0] - next_coord[0]
            dy = starting_coord[1] - next_coord[1]
            dl = math.sqrt(dx*dx + dy*dy)
            total += dl

    print(total)

if __name__ == '__main__':
    main()
