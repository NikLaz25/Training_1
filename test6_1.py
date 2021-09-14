def PatternUnlock(N, hits):
    length = 0
    big_len = 2**(1/2)
    for n in range(N - 1):
        xn_plus = abs(hits[n] + hits[n + 1])
        xn_minus = abs(hits[n] - hits[n + 1])
        if  xn_plus == 8 or xn_plus == 6 or (xn_plus == 9 and (xn_minus == 5 or xn_minus == 7)) or (xn_plus == 11 and (xn_minus == 5 or xn_minus == 6)):
            length += big_len
        else:
            length += 1

    my_str = str(round(length, 5))
    new_str = ''
    for i in my_str:
        if i != '0' and i != '.':
            new_str += i
    return new_str