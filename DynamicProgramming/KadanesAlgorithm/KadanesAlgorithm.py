def kadanes_algorithm(arr):
    """
    Kadane's Algorithm
    
    연속된 부분 수열 중 최대 합을 구하는 알고리즘


    Parameters:
        arr (List[int]): 정수 배열 (음수/양수 포함 가능)

    Returns:
        max_sum (int): 최대 연속 부분 수열의 합
        start (int): 최대 합을 이루는 부분 수열의 시작 인덱스
        end (int): 최대 합을 이루는 부분 수열의 끝 인덱스

    Time Complexity:
        O(N) - 배열을 한 번 순회하며 계산 (n = len(arr))
    """

    n = len(arr)

    max_sum = curr_sum = arr[0]     # 현재까지의 최대합과 현재 구간 합
    start = end = temp_start = 0    # 시작점, 끝점, 임시 시작점

    for i in range(1, n):
        # 현재 수 arr[i]부터 새로 시작하는 것이 기존 구간보다 이득인 경우
        if curr_sum + arr[i] < arr[i]:
            # 새로운 구간 시작
            curr_sum = arr[i]
            temp_start = i
        # 기존 구간의 합에 지금 수 arr[i]를 더하는 것이 더 큼
        else:
            curr_sum += arr[i]

        # 최대합 갱신
        if curr_sum > max_sum:
            max_sum = curr_sum
            start = temp_start
            end = i

    return max_sum, start, end

