import sys



def main0():
    """
    Для чтения входных данных необходимо получить их
    из стандартного потока ввода (sys.stdin).
    Данные во входном потоке соответствуют описанному
    в условии формату. Обычно входные данные состоят
    из нескольких строк.
    Можно использовать несколько методов:
    * input() -- читает одну строку из потока без символа
    перевода строки;
    * sys.stdin.readline() -- читает одну строку из потока,
    сохраняя символ перевода строки в конце;
    * sys.stdin.readlines() -- вернет список (list) строк,
    сохраняя символ перевода строки в конце каждой из них.
    Чтобы прочитать из строки стандартного потока:
    * число -- int(input()) # в строке должно быть одно число
    * строку -- input()
    * массив чисел -- map(int, input().split())
    * последовательность слов -- input().split()
    Чтобы вывести результат в стандартный поток вывода (sys.stdout),
    можно использовать функцию print() или sys.stdout.write().
    Возможное решение задачи "Вычислите сумму чисел в строке":
    print(sum(map(int, input().split())))
    """
    n, m = sys.stdin.readline().split()
    n = int(n)
    m = int(m)
    data = [list(map(int,input().split())) for i in range(n)]
    cache = [[(-1, '', ), ]*m for i in range(n)]

    def move(x, y, value_total, prev_path):
        if y == n:
            return -1, prev_path[:-2]
        if x == m:
            return -1, prev_path[:-2]

        if x + 1 < m and y + 1 < n:
            if cache[y][x + 1][0] > 0 and cache[y + 1][x][0] > 0:
                if cache[y][x + 1][0] > cache[y + 1][x][0]:
                    return cache[y][x + 1]
                else:
                    return cache[y + 1][x]

        value_here = data[y][x]

        value_right, path_right = move(x + 1, y, value_total, prev_path + ' R')
        value_down, path_down = move(x, y + 1, value_total, prev_path + ' D')

        if value_down == -1 and value_right == -1:
            # cache[y][x] = value_total + value_here, prev_path
            return value_total + value_here, prev_path

        if value_down == -1:
            # cache[y][x] = value_total + value_here + value_right, path_right
            return value_total + value_here + value_right, path_right

        if value_right == -1:
            # cache[y][x] = value_total + value_here + value_down, path_down
            return value_total + value_here + value_down, path_down

        if value_right > value_down:
            cache[y + 1][x] = value_total + value_here + value_right, path_right
            return value_total + value_here + value_right, path_right
        else:
            cache[y][x + 1] = value_total + value_here + value_down, path_down
            return value_total + value_here + value_down, path_down

    full_value, full_path = move(0, 0, 0, '')

    print(full_value)
    print(full_path.strip())



def main1():
    n, m = sys.stdin.readline().split()
    n = int(n)
    m = int(m)
    data=[list(map(int,input().split())) for i in range(n)]

    a = [[0]*m for i in range(n)]
    a[0][0] = data[0][0]

    for j in range(1, m):
        a[0][j] = a[0][j-1] + data[0][j]

    for i in range(1,n):
        a[i][0] = a[i-1][0] + data[i][0]

    for i in range(1,n):
        for j in range(1, m):
            a[i][j]=max(a[i][j-1], a[i-1][j]) + data[i][j]

    i = n-1
    j = m-1
    r = ''
    while i != 0 or j != 0:
        if j >= 1 and i >= 1:
            if a[i][j-1] > a[i-1][j]:
                r = 'R ' + r
            else:
                r = 'D ' + r
        else:
            if j >= 1:
                r = 'R ' + r
            else:
                r = 'D ' + r
        if r[0] == 'R':
            j -= 1
        else:
            i -= 1

    print(a[-1][-1])
    print(r.strip())



if __name__ == '__main__':
    main1()
