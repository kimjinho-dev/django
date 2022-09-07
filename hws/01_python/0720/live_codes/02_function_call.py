num1 = 0
num2 = 1


def func1(a, b):
    return a + b


def func2(a, b):
    return a - b


def func3(a, b):
    return func1(a, 5) + func2(5, b)  # func1과 func2를 호출


result = func3(num1, num2)  # func3을 호출
print(result)  # 9
