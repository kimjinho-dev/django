# 1. 함수는 '함수명()'으로 호출하며, return으로 결과값을 반환
def foo():
    return True


print(foo())  # True


# 2. 함수는 '함수명(인자)'로 호출하며, 인자는 함수에서 매개변수로 받아 값을 사용
# parameter(파라미터) == 매개변수
# argument(아규먼트) == 인자
def add(x, y):
    return x + y


print(add(2, 3))  # 5
