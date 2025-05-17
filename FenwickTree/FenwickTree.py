class FenwickTree:
    def __init__(self, size: int) -> None:
        """
        size: 배열의 크기
        self.tree: 누적합 저장용 트리 배열 (1-based 인덱스 사용)
        """

        self.tree = [] * (size + 1)
        self.size = size

    def update(self, idx: int, diff: int) -> None:
        """
        idx: 업데이트할 인덱스 (1-based)
        diff: 기존 값과 새로운 값의 차이
        """

        while idx <= self.size:
            self.tree[idx] += diff
            idx += idx & -idx

    def query(self, idx: int) -> int:
        result = 0

        while idx > 0:
            result += self.tree[idx]
            idx -= idx & -idx

        return result
    
    def range_query(self, left: int, right: int) -> int:
        """
        left, right: 구간의 시작과 끝 인덱스 (1-based)
        return: [left, right] 구간의 누적합
        """

        return self.query(right) - self.query(left - 1)

    