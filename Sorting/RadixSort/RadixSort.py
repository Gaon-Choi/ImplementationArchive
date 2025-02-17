def RadixSort(arr: list):
    max_k = len(str(max(arr)))
    max_digit = 10
    
    # 버킷
    buckets = [[] for _ in range(max_digit)]
    
    p = 0
    for pos in range(max_k):
        p = 10 ** pos
        
        # 각 요소의 자릿수에 맞추어 버킷에 넣음
        for elem in arr:
            buckets[(elem // p) % 10].append(elem)
            
        # 버킷 순서대로 arr에 담기
        arr.clear() # arr = []
        
        for bucket in buckets:
            arr.extend(bucket)
            
        # 버킷 초기화
        buckets = [[] for _ in range(max_digit)]
        
    return arr
