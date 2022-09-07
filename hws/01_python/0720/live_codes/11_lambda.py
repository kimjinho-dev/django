# lambda 함수 (== 익명함수, 한 줄로 간단하게 함수를 표현)
minus_two = lambda x: x - 2
result = minus_two(5)
print(result)

# map과 같이 사용 가능
minus_numbers = list(map(lambda x: x - 2, [5, 6]))
print(minus_numbers)
