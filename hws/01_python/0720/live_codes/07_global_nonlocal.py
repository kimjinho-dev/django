# 1. global
a = 10


def func1():
    global a  # 전역 변수를 변경하려면 global 키워드를 써야 함
    a = 3


func1()
print(a)


# 2. nonlocal
x = 0


def func1():
    x = 1

    def func2():
        nonlocal x  # 부모(상위) 함수의 변수를 변경하려면 nonlocal 키워드를 써야함
        x = 2

    func2()
    print(x)  # 2


func1()
print(x)  # 0
