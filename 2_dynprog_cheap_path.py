import sys


def main2():
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
    data = []
    for txt in sys.stdin.readlines():
        line = list(map(int, txt.strip().split()))
        data.append(line)

    def eat(x, y, kg_total):
        if y == n:
            return -1
        if x == m:
            return -1
        kg_here = data[y][x]

        kg_right = eat(x + 1, y, kg_total)
        kg_down = eat(x, y + 1, kg_total)

        if kg_down == -1 and kg_right == -1:
            return kg_total + kg_here

        if kg_down == -1:
            return kg_total + kg_here + kg_right

        if kg_right == -1:
            return kg_total + kg_here + kg_down

        if kg_right > kg_down:
            return kg_total + kg_here + kg_down
        else:
            return kg_total + kg_here + kg_right

    print(eat(0, 0, 0))



def main():
    import pprint
    n,m=map(int,input().split())
    p=[list(map(int,input().split())) for i in range(n)]
    pprint.pprint(p)
    a=[[0]*m for i in range(n)]
    a[0][0]=p[0][0]
    for j in range(1,m):
      a[0][j]=a[0][j-1]+p[0][j]
    pprint.pprint(a)
    for i in range(1,n):
      a[i][0]=a[i-1][0]+p[i][0]
    pprint.pprint(a)
    for i in range(1,n):
      for j in range(1,m):
        a[i][j]=min(a[i][j-1],a[i-1][j])+p[i][j]
    pprint.pprint(a)
    print(a[-1][-1])

if __name__ == '__main__':
    main()

