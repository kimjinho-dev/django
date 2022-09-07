# global
a = 0
b = 1


def enclosed():
    # enclosed
    a = 10
    c = 3

    def local(c):
        # local
        print(a, b, c)  # 10 1 300

    local(300)
    print(a, b, c)  # 10 1 3


enclosed()
print(a, b)  # 0 1
