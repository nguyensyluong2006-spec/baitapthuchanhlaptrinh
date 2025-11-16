def binary_search(arr, value):
    arr_sorted = sorted(arr)
    lower_bound = 0
    upper_bound = len(arr_sorted) - 1
    
    while lower_bound <= upper_bound:
        mid_point = (lower_bound + upper_bound) // 2
        
        if arr_sorted[mid_point] == value:
            return True
        elif arr_sorted[mid_point] < value:
            lower_bound = mid_point + 1
        else:
            upper_bound = mid_point - 1
    
    return False