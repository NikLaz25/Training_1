def odometer(my_list):
    distance = 0
    for i in range(len(my_list) - 1):
        if i % 2 == 0:
            speed = my_list[i]
            if i == 0:
                time = my_list[i + 1]
            else:
                time = my_list[i + 1] - my_list[i - 1]
            distance += speed * time
    return distance
