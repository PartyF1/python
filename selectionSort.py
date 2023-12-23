import time

def selectionSort(data, drawData, timer):
    n = len(data)
    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            # select the minimum element in every iteration
            if data[j] < data[min_index]:
                min_index = j
                drawData(data, ['Green' if x == j +
                                           1 else 'Red' for x in range(len(data))])
                time.sleep(timer)
        # swapping the elements to sort the array
        drawData(data, ['Blue' if (x == i or x==min_index) else 'Red' for x in range(len(data))])
        time.sleep(timer)
        (data[i], data[min_index]) = (data[min_index], data[i])
    drawData(data, ['Green' for x in range(len(data))])
