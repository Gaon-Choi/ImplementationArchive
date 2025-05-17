def get_ones_count(x):
    count = 0

    while x:
        count += x & 1  # 마지막 비트가 1인지 확인
        x >>= 1         # 오른쪽으로 1 비트 이동

    return count