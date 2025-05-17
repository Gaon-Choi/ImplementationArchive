def fast_exponent(a, k):
    if a == 0:
        return 1
    
    x = fast_exponent(a, k // 2)

    # 지수가 짝수일 때
    if k % 2 == 0:
        return x * x
    
    # 지수가 홀수일 때
    else:
        return x * x * a
    
def fast_exponent(a, k, mod):
    if a == 0:
        return 1
    
    x = fast_exponent(a, k // 2)

    # 지수가 짝수일 때
    if k % 2 == 0:
        return x * x % mod
    
    # 지수가 홀수일 때
    else:
        return x * x * a % mod