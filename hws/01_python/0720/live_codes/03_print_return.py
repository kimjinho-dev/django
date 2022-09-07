# 1. Void function -> None을 반환
def void_product(x, y):
    print(f'{x} x {y}')
    # return None 이 생략되어 있음


void_product(4, 5)  # 4 x 5
print(void_product(4, 5))  # None도 같이 출력


# 2. Value returning function -> 값을 반환
def value_returning_product(x, y):
    return x * y


ans = value_returning_product(4, 5)
print(ans)  # 20
