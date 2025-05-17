def shunting_yard(expression : str) -> str:
    operators = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2
    }

    output = []
    stack = []

    for token in expression:
        # 피연산자(A-Z, 0-9 등)
        if token.isalnum():
            output.append(token)

        elif token == "(":
            stack.append(token)

        elif token == ")":
            # "("가 나올 때까지 pop을 수행
            while stack and stack[-1] != "(":
                output.append(stack.pop())

            # "(" 삭제
            stack.pop()

        else:
            # 연산자 우선순위 비교
            # 현재 연산자의 우선순위보다 높은 연산자 모두 처리
            while stack and (stack[-1] != "(") and (operators.get(stack[-1], 0) >= operators[token]):
                output.append(stack.pop())
            
            stack.append(token)

    # 남은 연산자를 모두 pop
    while stack:
        output.append(stack.pop())

    return "".join(output)