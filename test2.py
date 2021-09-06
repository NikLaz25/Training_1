def odometer(oksana):
    distance = 0
    for i in range(len(oksana) - 1):
        if i % 2 == 0:
            speed = oksana[i]
            if i == 0:
                time = oksana[i + 1]
            else:
                time = oksana[i + 1] - oksana[i - 1]
            distance += speed * time
    return distance
