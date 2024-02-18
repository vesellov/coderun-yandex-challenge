
def max_ones_after_remove_item(inp):
    seq = []
    last_v = None
    max_ones_length = 0

    if len(inp) == 1:
        print(0, inp)
        return 0

    for i in range(len(inp + '0')):
        if i == len(inp):
            v = 0
        else:
            v = int(inp[i])

        if last_v is None:
            last_v = v
            seq.append([v, 1, ])
            continue

        if last_v == v:
            # same value, did not switch
            seq[-1][1] += 1
            if v == 1:
                if seq[-1][1] > max_ones_length:
                    max_ones_length = seq[-1][1]

        else:
            # switch 0 <-> 1
            last_v = v
            if v == 0 and seq:
                # switch 1 -> 0
                if seq[-1][1] > max_ones_length:
                    max_ones_length = seq[-1][1]
            seq.append([v, 1, ])

            if v == 0:
                # switch 1 -> 0
                if len(seq) > 3:
                    if seq[-3][1] == 1:
                        max_ones_length = max(max_ones_length, seq[-4][1] + seq[-2][1])

    # take care of the last artificially added sequence of one single zero element
    if len(seq) == 2 and seq[-1][1] == 1:
        max_ones_length = seq[0][1] - 1

    print(max_ones_length, inp)

    return max_ones_length


assert 0 == max_ones_after_remove_item('0')
assert 0 == max_ones_after_remove_item('1')
assert 1 == max_ones_after_remove_item('10')
assert 2 == max_ones_after_remove_item('101')
assert 1 == max_ones_after_remove_item('010')
assert 1 == max_ones_after_remove_item('11')
assert 0 == max_ones_after_remove_item('0000')
assert 3 == max_ones_after_remove_item('1111')
assert 2 == max_ones_after_remove_item('011')
assert 3 == max_ones_after_remove_item('1101')
assert 3 == max_ones_after_remove_item('11010')
assert 5 == max_ones_after_remove_item('10111100111010101')
assert 4 == max_ones_after_remove_item('1011100111010101')
assert 7 == max_ones_after_remove_item('1011110111010101')
assert 6 == max_ones_after_remove_item('101110111010101')
assert 5 == max_ones_after_remove_item('101101011101101')
assert 5 == max_ones_after_remove_item('101101011101100')
assert 6 == max_ones_after_remove_item('10110101110111')
assert 7 == max_ones_after_remove_item('10010111110110')
