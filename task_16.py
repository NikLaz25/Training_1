# создаем метод
def MaximumDiscount(N, price):
    # сортируем по убыванию
    price.sort(reverse = True)
    
    # вычисляем, какое количество элементов оставить
    # отсекаем хвост
    price = price[:(len(price) // 3 * 3)]    
    
    # разбиваем по 3 элемента
    N_3 = len(price) // 3
    price_group = []
    for i in range(0, len(price),3):
        price_group += [price[i:(i + 3)]]
    
    # в каждой покупке находим минимум, и добавляем к итогу
    result = 0
    for i in price_group:
        result += min(i)
    return result