def MergeSort(arr: list):
    # Base Case : 배열의 길이가 1인 경우
    if len(arr) <= 1:
        return arr
        
    # 중간점 찾기
    mid = len(arr) // 2
    
    # 중간점을 기점으로 리스트 쪼개기
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # 두 개의 서브 배열로 쪼개어 정렬 수행
    left_sorted = MergeSort(left_half)
    right_sorted = MergeSort(right_half)
    
    # 두 개의 정렬된 서브 배열을 하나로 합침
    return _Merge(left_sorted, right_sorted)
    
def _Merge(left, right):
    sorted_array = []
    
    # i : left, j : right
    i = 0; j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
            
    # 두 개의 서브 배열의 남은 원소 넣기 (둘 중 하나만 빈 상태)
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    
    return sorted_array
