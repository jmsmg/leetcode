array = list(map(int, input().split()))

for i in range(len(array) - 1):
    tmp = i
    for j in range(i+1, len(array)):
        if array[tmp] > array[j]:
            tmp = j
    array[i], array[tmp] = array[tmp], array[i]
    
print(array)