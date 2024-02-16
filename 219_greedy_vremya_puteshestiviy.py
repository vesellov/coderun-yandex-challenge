import sys


def main():
    data = list(map(int, input().split()))

    temperature_index = {}
    for i in range(len(data)):
        temperature = data[i]
        if temperature not in temperature_index:
            temperature_index[temperature] = []
        temperature_index[temperature].append(i)

    max_temperature_diff = -1
    min_days_diff = -1
    best_day_start = -1
    best_day_end = -1

    for temperature_start in range(1, 46):

        for temperature_start_index in temperature_index.get(temperature_start, []):

            for temperature_end in range(45, temperature_start, -1):

                if temperature_end - temperature_start < max_temperature_diff:
                    break

                temperature_end_index = temperature_start_index

                for temperature_end_index in temperature_index.get(temperature_end, []):

                    if temperature_start_index >= temperature_end_index:
                        continue

                    temperature_diff = temperature_end - temperature_start

                    if max_temperature_diff == -1:
                        max_temperature_diff = temperature_diff

                        days_diff = temperature_end_index - temperature_start_index

                        if min_days_diff == -1:
                            min_days_diff = days_diff
                            min_days_diff = days_diff
                            best_day_start = temperature_start_index
                            best_day_end = temperature_end_index

                        if min_days_diff > days_diff:
                            min_days_diff = days_diff
                            best_day_start = temperature_start_index
                            best_day_end = temperature_end_index

                    if max_temperature_diff < temperature_diff:
                        max_temperature_diff = temperature_diff

                        days_diff = temperature_end_index - temperature_start_index

                        if min_days_diff == -1:
                            min_days_diff = days_diff
                            min_days_diff = days_diff
                            best_day_start = temperature_start_index
                            best_day_end = temperature_end_index

                        if min_days_diff > days_diff:
                            min_days_diff = days_diff
                            best_day_start = temperature_start_index
                            best_day_end = temperature_end_index

    print(max_temperature_diff, best_day_start, best_day_end)

if __name__ == '__main__':
    main()
