import sys

def ft_merge_sort(array:list) -> list:
    
    if len(array) < 2:
        return array
    
    pivot = len(array) // 2
    
    left_array = ft_merge_sort(array[:pivot])
    right_array = ft_merge_sort(array[pivot:])

    l = 0
    r = 0

    while l 

array = list(map(int, sys.stdin.readline().split())

print(array)