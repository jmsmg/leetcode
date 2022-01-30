def binary_search(answer:list, pop_number:int) -> list:
    if pop_number < answer[0]:
        return answer.insert(0, pop_number)
        
    elif pop_number > answer[-1]:
        return answer.append(pop_number)
    
    L = 0
    R = len(answer) - 1
    
    while L >= R:
        pivot = L + R // 2
        
        if answer[pivot] < pop_number:
            L = pivot+1
        elif answer[pivot] > pop_number:
            R = pivot
    
    return answer.insert(R+1, pop_number)
    
unsorted = list(map(int, input().split()))

if unsorted != []:
    answer = [unsorted.pop(0)]
    
    for i in range(len(unsorted)):
        pop_number = unsorted.pop(0)
        
        binary_search(answer, pop_number)
else:
    answer = -1

print(answer)