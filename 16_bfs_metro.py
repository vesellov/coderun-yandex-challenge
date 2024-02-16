import sys


def main():
    n = int(input())
    m = int(input())
    inp_lines = sys.stdin.readlines()
    a, b = inp_lines[-1].split()
    a = int(a)
    b = int(b)

    metro_lines = []

    for inp_line in inp_lines[:-1]:
        metro_lines.append(tuple([int(i) for i in inp_line.split()[1:]]))

    graph_stations = {}
    graph_lines = {}
    graph_indexed = {}

    for metro_line_id in range(len(metro_lines)):
        metro_line_stations = metro_lines[metro_line_id]
        graph_lines[metro_line_id] = set(metro_line_stations)
        for metro_station in metro_line_stations:
            if metro_station not in graph_stations:
                graph_stations[metro_station] = set()
            graph_stations[metro_station].add(metro_line_id)
    
    for metro_line_id in range(len(metro_lines)):
        metro_line_stations = tuple(sorted(metro_lines[metro_line_id]))
        if metro_line_id not in graph_indexed:
            graph_indexed[metro_line_id] = set()
        for metro_station in metro_line_stations:
            for another_metro_line_id in graph_stations[metro_station]:
                another_metro_line_stations = tuple(sorted(metro_lines[another_metro_line_id]))
                graph_indexed[metro_line_id].add(another_metro_line_id)

    # print(graph_lines)
    # print(graph_stations)
    # print(graph_indexed)

    visited_line_ids = []
    queue = []
    for metro_line_id in graph_stations[a]:
        queue.append([metro_line_id, ])

    while queue:
        current_path = queue.pop(0)
        current_metro_line_id = current_path[-1]
        
        if current_metro_line_id not in visited_line_ids:

            for metro_line_id in graph_indexed[current_metro_line_id]:

                new_path = list(current_path)
                if metro_line_id not in new_path:
                    new_path.append(metro_line_id)
                queue.append(new_path)

                if b in graph_lines[metro_line_id]:
                    print(len(new_path) - 1)
                    print(new_path)
                    print([graph_lines[i] for i in new_path])
                    return

            visited_line_ids.append(current_metro_line_id)

    print(-1)

if __name__ == '__main__':
    main()