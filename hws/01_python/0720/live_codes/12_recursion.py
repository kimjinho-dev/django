# 재귀 함수란 자기 자신을 호출하며 점점 깊게 들어가는 함수
# 재귀의 깊이가 깊어질 때 마다 범위가 작아짐
# base-case(재귀탈출조건)과 점화식으로 이루어짐

# 팩토리얼
def factorial(n):
    # 1. base case (재귀탈출조건)
    if n <= 1:
        return 1

    # 2. 점화식
    return n * factorial(n - 1)


print(factorial(4))  # 24
