def BinarySearch(arr: list[int], target: int):
    left = 0; right = n - 1

    idx = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            idx = mid
            break

        # 현재의 중앙이 찾는 값보다 크거나 같은 경우
        if arr[mid] > target:
            # 오른쪽을 줄여야 함
            right = mid - 1
        else:
            left = mid + 1

    return idx