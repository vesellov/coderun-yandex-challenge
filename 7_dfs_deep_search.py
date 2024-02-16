import sys

sys.setrecursionlimit(150000)


def main():
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

    routes = []
    for line in sys.stdin.readlines():
        if line.strip():
            p1, p2 = line.strip().split(' ')
            routes.append((int(p1), int(p2), ))

    points = {}
    first_point = 1000000
    for route in routes:
        p1 = route[0]
        p2 = route[1]
        first_point = min(first_point, min(p1, p2))
        if p1 not in points:
            points[p1] = set()
        if p2 not in points[p1]:
            points[p1].add(p2)
        if p2 not in points:
            points[p2] = set()
        if p1 not in points[p2]:
            points[p2].add(p1)

    point1set = set()
    cache = {}

    def dfs(start, visited=None):
        if visited is None:
            visited = set()
        if start in cache:
            visited.update(cache[start])
            return visited
        visited.add(start)
        if start in points:
            for point in points[start] - visited:
                dfs(point, visited)
        cache[start] = visited
        return visited

    point1set = list(dfs(1))
    point1set.sort()

    print(len(point1set))
    print(' '.join(map(str, point1set)))

if __name__ == '__main__':
    main()
