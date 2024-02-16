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
    for route in routes:
        p1 = route[0]
        p2 = route[1]
        if p1 not in points:
            points[p1] = set()
        if p2 not in points[p1]:
            points[p1].add(p2)
        if p2 not in points:
            points[p2] = set()
        if p1 not in points[p2]:
            points[p2].add(p1)

    # cache = {}
    components = {}
    used = set()
    all_points = set(range(1, n + 1))

    def dfs(start, current, visited=None):
        # print(start, current, used)
        if visited is None:
            visited = set()
        used.add(current)
        # if current in cache:
        #     visited.update(cache[current])
        #     return visited
        visited.add(current)
        if current in points:
            for point in points[current] - visited:
                if point not in used:
                    dfs(start, point, visited)
        # cache[current] = visited
        # for point in visited:
        #     cache[point] = visited
        # if start == current:
        #     component_tuple = tuple(sorted(list(visited)))
        #     if component_tuple not in components:
        #         components.append(component_tuple)
        return visited

    cur_component = 0
    while len(all_points):
        point = all_points.pop()
        component = dfs(point, point)
        components[cur_component] = component
        for component_point in component:
            all_points.discard(component_point)
        cur_component += 1

    # for point in range(1, n + 1):
    #     component = dfs(point, point)
        # component_tuple = tuple(sorted(list(component)))
        # if component_tuple not in components:
        #     components.append(component_tuple)

    print(len(components))
    for component in components.values():
        print(len(component))
        print(' '.join(map(str, component)))


if __name__ == '__main__':
    main()