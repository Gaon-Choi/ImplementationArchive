def lower_bound(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left

def longest_increasing_subsequence(arr):
    # 시간 복잡도 : O(NlogN)

    # DP : dp[i]는 길이 i+1의 증가 부분 수열을 만들 수 있는 가장 작은 끝 값
    dp = []

    # lis_result[i]는 i번째 원소까지의 prefix에서, 해당 인덱스까지 고려하여 만들 수 있는 LIS의 "길이" 중 num이 들어갈 수 있는 위치(index) + 1
    # arr[i]를 고려했을 때, 길이 X의 증가 부분 수열에서 X = lis_result[i] 로서 arr[i]는 그 자리에 올 수 있는 최소의 수가 된다.
    lis_result = [0] * len(arr)
    
    for i, num in enumerate(arr):
        # num이 들어갈 수 있는 가장 왼쪽 위치 (이진 탐색으로 O(log N))
        bis_idx = lower_bound(dp, num)

        # dp의 모든 원소보다 크다면 해당 원소를 추가
        if bis_idx == len(dp):
            dp.append(num)
        # 아니라면 해당 인덱스의 값을 교체
        else:
            dp[bis_idx] = num

        lis_result[i] = bis_idx + 1

    return lis_result
