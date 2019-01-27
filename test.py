def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot



def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
    return _quicksort(array, begin, end)



array = ["22/12/2018 13:07 PM","22/12/2018 14:07 PM","22/12/2018 13:46 PM","22/12/2018 14:46 PM","22/12/2018 15:07 PM","22/12/2018 15:46 PM","22/12/2018 15:56 PM"]
quicksort(array)

print(array)