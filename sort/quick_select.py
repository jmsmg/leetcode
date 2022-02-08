def quick_select(array:list, rank:int) -> int:
    if len(array) < 2:
        return -1

    L = 0
    R = len(array) - 2
    array[len(array)-3], array[len(array)-1] = array[len(array)-1], array[len(array)-3]
    pivot = len(array)-1 

    while L < R:
        if array[L] < array[pivot]:
            L =+ 1
        if array[pivot] < array[R]:
            R =- 1
        if array[L] > array[pivot] and array[R] < array[pivot]:
            array[L], array[R] = array[R], array[L]

    array[L], array[pivot] = array[pivot], array[L]

    if L < rank:
        return quick_select(array[R:], rank) +
    elif R > rank:
        return quick_select(array[:L], rank)

array = list(map(int, input().split()))
rank = int(input())

print(quick_select(array, rank))