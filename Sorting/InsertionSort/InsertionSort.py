def InsertionSort(arr: list):
    N = len(arr)
    
    for i in range(1, N):
        j = i - 1
        key = arr[i]

        # 현재 위치보다 앞에 있는 원소 중 삽입할 위치 탐색
        while j >= 0 and arr[j] > key:
            # 원소를 오른쪽으로 한칸씩 밀어낸다
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key
