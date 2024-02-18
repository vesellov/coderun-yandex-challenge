import sys

from functools import cmp_to_key

smallest_diff = -1

def main1():
    global smallest_diff
    n = int(input())

    for _ in range(n):
        m = int(input())
        data = list(map(int, input().split()))

        smallest_diff = -1

        def compare(a, b):
            global smallest_diff
            diff = a ^ b
            if smallest_diff == -1:
                smallest_diff = diff
            if smallest_diff > diff:
                smallest_diff = diff
            return a - b

        data.sort(key=cmp_to_key(compare))

        print(smallest_diff)

    
def main2():
    n = int(input())
    for _ in range(n):
        m = int(input())
        data = list(map(int, input().split()))
        data.sort()

        min_diff = data[0] ^ data[1]
        for i in range(1, m):
            min_diff = min(min_diff, data[i-1] ^ data[i])
            
        print(min_diff)

        
if __name__ == '__main__':
    main2()
