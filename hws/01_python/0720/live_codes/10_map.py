# 내장함수 map (특정 함수를 컨테이너의 원소에 각각 적용한 결과를 반환)
int_numbers = map(int, ["1", "2", "3"])

print(int_numbers)  # map 객체가 나오므로 리스트로 변환해야 함
print(list(int_numbers))


# 사용자 정의 함수도 map과 사용 가능
def minus_two(x):
    return x - 2


minus_numbers = list(map(minus_two, [5, 6]))
print(minus_numbers)
