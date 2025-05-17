def build_pi(pattern):
    m = len(pattern)
    pi = [0] * m

    j = 0

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j

    return pi

def kmp_search(data, pattern):
    n, m = len(data), len(pattern)

    pi = build_pi(pattern)

    j = 0

    for i in range(n):
        while j > 0 and data[i] != pattern[j]:
            j = pi[j - 1]

        if data[i] == pattern[j]:
            j += 1

            # 패턴의 길이에 도달한 경우
            if j == m:
                return True

    return False
