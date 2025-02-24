def _Partition(arr, low, high):
    # 피벗으로 가장 오른쪽에 있는 원소를 결정
    pivot = arr[high]
    
    i = low - 1
    
    # 모든 원소들을 순회하며 피벗 값과 비교
    for j in range(low, high):
        if arr[j] <= pivot:
            # 피벗보다 큰 값을 발견하면 인덱스 i의 값과 스와핑
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    return i + 1

def QuickSort(arr: list, low = 0, high = len(arr) - 1):
    
    if low < high:
        pivot = _Partition(arr, low, high)
        
        # 재귀적으로 피벗 기준 왼쪽, 오른쪽 배열에 대해 호출
        QuickSort(arr, low, pivot - 1)
        QuickSort(arr, pivot + 1, high)
