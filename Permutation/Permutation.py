'''
순열(Permutation)

순서 0, 중복 X
'''

def permutation(arr, n):
    result = []
    permutation = []
    
    visited = [False] * len(arr)

    def backtrack():
        # 순열열 n개가 되면 결과 추가
        if len(permutation) == n:
            result.append(permutation[:])
            return

        # 리스트 전체 범위 원소에서 조합 선택
        for i in range(len(arr)):
            if not visited[i]:
                visited[i] = True
                
                # 현재 원소 선택
                permutation.append(arr[i])
                # 다음 원소로 넘어감
                backtrack()
                # 마지막에 선택한 원소를 제거하고 돌아감
                permutation.pop()
                
                visited[i] = False

    backtrack()

    return result
