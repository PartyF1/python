import time

def merge_sort(data, drawData, start, end, timer):
    #Sorts the list from indexes start to end - 1 inclusive
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(data, drawData, start, mid, timer)
        merge_sort(data, drawData, mid, end, timer)
        merge_list(data, drawData, start, mid, end,timer)
        drawData(data, ['Green' for x in range(len(data))])
        time.sleep(timer)

def merge_list(data, drawData, start, mid, end,timer):
    left = data[start:mid]
    right = data[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            data[k] = left[i]
            i = i + 1
        else:
            data[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            data[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            data[k] = right[j]
            j = j + 1
            k = k + 1