def lower_bound(arr: list, target):
    left = 0
    right = len(arr) - 1
    
    min_idx = len(arr)  # 최소이므로 답이 될 수 있는 값보다 크게 설정
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] >= target:
            right = mid - 1
            min_idx = min(min_idx, mid)
        else:
            left = mid + 1
            
    return min_idx
