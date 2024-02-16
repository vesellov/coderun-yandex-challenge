import sys


def main():
    n = int(input())

    cube = {}
    start = None

    for level in range(n):
        sys.stdin.readline()
        for col in range(n):
            line = sys.stdin.readline()
            row = 0
            for char in line:
                cube[(level+1, col+1, row+1, )] = True if char == '#' else False
                if char == 'S':
                    start = (level+1, col+1, row+1, )
                row += 1

    directions = ((-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1), )

    def way_up(start_point):
        if start_point[0] == 1:
            return [start_point, ]

        result = []

        prev_point_matrix = {}
        prev_point_matrix[start_point] = None
        next_points_list = [start_point, ]

        for base_point in next_points_list:

            end_point = None
            for new_point_delta in directions:
                new_point = (
                    base_point[0] + new_point_delta[0],
                    base_point[1] + new_point_delta[1],
                    base_point[2] + new_point_delta[2],
                )

                if 1 <= new_point[0] <= n and 1 <= new_point[1] <= n and 1 <= new_point[2] <= n:
                    if not cube[new_point]:
                        if new_point not in prev_point_matrix:
                            prev_point_matrix[new_point] = base_point
                            next_points_list.append(new_point)
                            if new_point[0] == 1:
                                end_point = new_point

            if end_point:
                prev_point = end_point
                result = [prev_point, ]
                while prev_point_matrix[prev_point]:
                    prev_point = prev_point_matrix[prev_point]
                    result.append(prev_point)
                result.reverse()
                break

        return result

    print(len(way_up(start)) - 1)


if __name__ == '__main__':
    main()
