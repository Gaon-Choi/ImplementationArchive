def Combination(arr, n):
    result = []
    combination = []

    def backtrack(start):
        # 조합 n개가 되면 결과 추가
        if len(combination) == n:
            result.append(combination[:])
            return

        # 리스트 원소에서 조합 선택 (겹치지 않아야 하므로 시작점부터 수행)
        for i in range(start, len(arr)):
            # 현재 원소 선택
            combination.append(arr[i])
            # 다음 원소로 넘어감
            backtrack(i + 1)
            # 마지막에 선택한 원소를 제거하고 돌아감
            combination.pop()

    backtrack(0)

    return result
