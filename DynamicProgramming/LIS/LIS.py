def longest_increasing_subsequence(arr):
    size = len(arr)

    # 최소 길이는 1
    lis = [1] * size

    # 경로 추적용 리스트
    # prev[i] = i 이전에 연결된 인덱스
    prev = [-1] * size

    max_length = 1
    max_idx = 0

    for i in range(size):
        for j in range(i):
            # 증가하는 구간이면 최장 수열 길이 갱신
            if arr[j] < arr[i] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                prev[i] = j

        if lis[i] > max_length:
            max_length = lis[i]
            max_idx = i

    lis_sequence = []

    while max_idx != -1:
        lis_sequence.append(arr[max_idx])
        max_idx = prev[max_idx]

    # 뒤에서부터 쌓았으므로 순서 뒤집기
    lis_sequence.reverse()

    return max_length, lis_sequence
