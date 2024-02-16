import sys


def main():
    n, m, s, t, q = map(int, input().split())
    blohi_list = list(map(lambda line: tuple(map(int, line.split())), sys.stdin.readlines()))

    backward_cache = {}
    cache_matrix = [[None for _ in range(m)] for _ in range(n)]

    directions = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1), )

    def build_backward_cache(end_point):
        backward_cache[end_point] = None
        next_points_list = [end_point, ]

        for base_point in next_points_list:

            for new_point_delta in directions:
                new_point = (base_point[0] + new_point_delta[0], base_point[1] + new_point_delta[1])

                if 1 <= new_point[0] <= n and 1 <= new_point[1] <= m:
                    if new_point not in backward_cache:
                        backward_cache[new_point] = base_point
                        next_points_list.append(new_point)


    def bloha(end_point, start_point):

        if end_point == start_point:
            return 0

        result = []

        if start_point in backward_cache:
            prev_point = start_point
            result = [prev_point, ]
            while backward_cache[prev_point]:
                prev_point = backward_cache[prev_point]
                result.append(prev_point)
            result.reverse()
            return len(result) - 1

        if cache_matrix[start_point[0]-1][start_point[1]-1] is not None:
            return cache_matrix[start_point[0]-1][start_point[1]-1]

        prev_point_matrix = {}
        prev_point_matrix[start_point] = None
        next_points_list = [start_point, ]

        for base_point in next_points_list:

            for new_point_delta in directions:
                new_point = (base_point[0] + new_point_delta[0], base_point[1] + new_point_delta[1])

                if 1 <= new_point[0] <= n and 1 <= new_point[1] <= m:
                    if new_point not in prev_point_matrix:
                        prev_point_matrix[new_point] = base_point
                        next_points_list.append(new_point)

            if end_point in prev_point_matrix:
                prev_point = end_point
                result = [prev_point]
                while prev_point_matrix[prev_point]:
                    prev_point = prev_point_matrix[prev_point]
                    result.append(prev_point)
                result.reverse()
                break

        if result:
            for i in range(len(result) - 1):
                point = result[i]
                cache_matrix[point[0]-1][point[1]-1] = len(result[i:]) - 1

        return len(result) - 1


    build_backward_cache((s, t, ))

    total = 0

    for bloha_coord in blohi_list:
        bloha_path_len = bloha((s, t, ), (bloha_coord[0], bloha_coord[1], ), )
        if bloha_path_len < 0:
            print(-1)
            return
        total += bloha_path_len

    print(total)


if __name__ == '__main__':
    main()