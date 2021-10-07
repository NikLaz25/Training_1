def UFO(N, data, octal):
    if octal == False:
        system = 16

    else:
        system = 8
    new_data = []
    
    for i in range(N):
        new_data += [int(str(data[i]), system)]

    return new_data