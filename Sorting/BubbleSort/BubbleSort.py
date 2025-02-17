def BubbleSort(arr: list):
    N = len(arr)
    
    # 아래의 행위를 N번 반복
    for _ in range(N):
        
        # 인접한 원소끼리 비교하여 스와핑
        for i in range(N - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
