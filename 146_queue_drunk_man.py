import sys


def main():
    player1 = list(map(int, input().split()))
    player2 = list(map(int, input().split()))

    turn_id = 0

    while player1 and player2:
        if turn_id >= 1000000:
            break

        player1card = player1.pop(0)
        player2card = player2.pop(0)

        win = None
        if player1card == 0 and player2card == 9:
            win = 'first'
        elif player2card == 0 and player1card == 9:
            win = 'second'
        elif player1card > player2card:
            win = 'first'
        elif player2card > player1card:
            win = 'second'

        if win == 'first':
            player1.append(player1card)
            player1.append(player2card)
        else:
            player2.append(player1card)
            player2.append(player2card)

        turn_id += 1

    if turn_id >= 1000000:
        print('botva')
    else:
        if player1:
            print('first', turn_id)
        else:
            print('second', turn_id)


if __name__ == '__main__':
    main()