def PatternUnlock(N, hits):
    my_str = str(N*(100000))
    new_str = ''
    for i in my_str:
        if i != '0' and i != '.':
            new_str += i
    return new_str