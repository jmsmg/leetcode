def ft_recur_merge(array:list) -> list:

    if len(array) < 2:
        return array

    mid = len(array) // 2

    left_sorted = ft_recur_merge(array[:mid])
    right_sorted = ft_recur_merge(array[mid:])
    
    merged_array = []
    
    left_idx = 0
    right_idx = 0
    
    while left_idx < len(left_sorted) and right_idx < len(right_sorted):
        if left_sorted[left_idx] <= right_sorted[right_idx]:
            merged_array.append(left_sorted[left_idx])
            left_idx += 1
        else:
            merged_array.append(right_sorted[right_idx])
            right_idx += 1

    merged_array += left_sorted[left_idx:]
    merged_array += right_sorted[right_idx:]

    return merged_array

array = list(map(int, input().split()))

print(ft_recur_merge(array))