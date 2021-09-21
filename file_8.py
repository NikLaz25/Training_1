
def SumOfThe(N, data):
    for n in range(N):
        my_sum = sum(data) - data[n]
        if my_sum == data[n]:
            return my_sum

