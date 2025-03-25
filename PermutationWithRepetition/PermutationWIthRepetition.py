'''
중복 순열(Permutation with Repetition; Product)

순서 0, 중복 0
'''

def permutation_with_repetition(arr, n):
    result = []
    product = []

    def backtrack():
        # 조합 n개가 되면 결과 추가
        if len(product) == n:
            result.append(product[:])
            return

        # 리스트 전체 범위 원소에서 조합 선택
        for i in range(len(arr)):
            # 현재 원소 선택
            product.append(arr[i])
            # 다음 원소로 넘어감
            backtrack()
            # 마지막에 선택한 원소를 제거하고 돌아감
            product.pop()

    backtrack()

    return result