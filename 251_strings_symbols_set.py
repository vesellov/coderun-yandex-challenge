import sys


def main():
    input_str = input()
    input_set = input()

    in_set = set(input_set)

    min_len = -1
    for i in range(len(input_str)):
        for j in range(i+1, len(input_str)+1):
            sub_str = input_str[i:j]
            if set(sub_str) == in_set:
                if min_len < 0:
                    min_len = len(sub_str)
                if min_len > len(sub_str):
                    min_len = len(sub_str)

    print(max(0, min_len))

if __name__ == '__main__':
    main()
