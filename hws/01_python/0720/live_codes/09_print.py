# 출력 (내장함수 print는 기본적으로 출력 후 한 줄 개행 / end와 sep 옵션)
a, b, c = "Hello", "Python", "!"
print(a)
print(a, b, c)  # 콤마로 구분된 원소는 공백을 기준으로 띄어서 출력

print(a, end="-")  # end 옵션은 출력 후 맨 끝 문자를 지정
print(b)
print(c)

print(a, b, c, sep="-")  # sep 옵션은 출력되는 각 원소 사이 문자를 지정
print(a, b, c, sep="\n")
