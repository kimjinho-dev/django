# 1. 튜플 패킹과 언패킹
numbers = 1, 2, 3, 4, 5  # 패킹
print(numbers)  # (1, 2, 3, 4, 5)

a, b, c, d, e = (1, 2, 3, 4, 5)  # 언패킹
print(a, b, c, d, e)  # 1 2 3 4 5


# 2. asterisk를 이용한 패킹과 언패킹
# 위치 가변인자(*args) -> 낱개로 들어오는 위치 인자들을 튜플로 패킹
def add(*args):
    for arg in args:
        print(arg)


# 가변인자는 인자의 개수가 계속 달라질 때 사용
add(2)  # 한 개의 인자도 가능
add(2, 3, 4, 5)  # 여러 개의 인자도 가능

values = [1, 2, 3, 4, 5]
add(*values)  # value의 괄호를 떼고 낱개로 언패킹하여 add 함수의 인자로 넣음


# 키워드 가변인자(**kwargs) -> 낱개로 들어오는 키워드 인자들을 딕셔너리로 패킹
def keyword_args(**kwargs):
    print(kwargs)
    print(type(kwargs))


keyword_args(a=1, b=2, c=3)
