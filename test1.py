def squirrel(N):
    factl = 1
    while N > 1:
        factl *=  N
        N -= 1
    return int(str(factl)[0])
