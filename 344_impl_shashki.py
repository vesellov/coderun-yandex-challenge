import sys


def main():
    n, m = map(int, input().split())
    whites = set()
    white_number = int(input())
    for _ in range(white_number):
        whites.add(tuple(map(int, input().split())))
    blacks = set()
    black_number = int(input())
    for _ in range(black_number):
        blacks.add(tuple(map(int, input().split())))
    first_turn = input()

    directions = (
        ((-2, -2, ), (-1, -1, ), ),
        ((2, -2, ), (1, -1, ), ),
        ((-2, 2, ), (-1, 1, ), ),
        ((2, 2, ), (1, 1, ), ),
    )

    if first_turn == 'white':

        for white_shashka in whites:
            for step, half_step in directions:
                possible_white_shashka_move = (
                    white_shashka[0] + step[0],
                    white_shashka[1] + step[1],
                )
                possible_black_shashka = (
                    white_shashka[0] + half_step[0],
                    white_shashka[1] + half_step[1],
                )
                if 1 <= possible_white_shashka_move[0] <= n and 1 <= possible_white_shashka_move[1] <= m:
                    if possible_white_shashka_move not in whites and possible_white_shashka_move not in blacks:
                        if possible_black_shashka in blacks:
                            print('Yes')
                            return

    else:

        for black_shashka in blacks:
            for step, half_step in directions:
                possible_black_shashka_move = (
                    black_shashka[0] + step[0],
                    black_shashka[1] + step[1],
                )
                possible_white_shashka = (
                    black_shashka[0] + half_step[0],
                    black_shashka[1] + half_step[1],
                )
                if 1 <= possible_black_shashka_move[0] <= n and 1 <= possible_black_shashka_move[1] <= m:
                    if possible_black_shashka_move not in whites and possible_black_shashka_move not in blacks:
                        if possible_white_shashka in whites:
                            print('Yes')
                            return

    print('No')

if __name__ == '__main__':
    main()
