import time

def insertion_sort(data, drawData, timer):
    """ сортировка вставками """
    n = len(data)
    # итерация по неотсортированным массивам
    for i in range(1, n):

        # получаем значение элемента
        val = data[i]

        # записываем в hole индекс i
        hole = i

        # проходим по массиву в обратную сторону, пока не найдём элемент больше текущего
        while hole > 0 and data[hole - 1] > val:
            # переставляем элементы местами , чтобы получить правильную позицию
            data[hole] = data[hole - 1]
            drawData(data, ['Green' if x == hole
                                       else 'Red' for x in range(len(data))])
            time.sleep(timer)

            # делаем шаг назад
            hole -= 1

        # вставляем значение на верную позицию
        data[hole] = val
    drawData(data, ['Green' for x in range(len(data))])