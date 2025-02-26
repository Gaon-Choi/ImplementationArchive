def upper_bound(arr: list, target):
    left = 0
    right = len(arr) - 1
    
    min_idx = right
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] > target:
            right = mid - 1
            min_idx = min(min_idx, mid)
        else:
            left = mid + 1
            
    return min_idx
