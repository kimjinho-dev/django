# 20220727 homework

## 1. Type Class

```
math
int
dict
list
float
```

## 2. Magic MEthod

```
__init__ : 생성자. 객체 생성시 작동
__del__ : 제거할때 실행. 객체가 삭제될때 작동
__str__ : 객체의 출력방식을 지정
__repr__ : __str__과 같이 출력방식을 지정하는것인데, str은 문자열방식으로 출력하는데에 반해, repr는 사람이 읽을 수 있도록, 표현을 하는것.
```

## 3. Instance Method

```
.pop() : 랜덤한 인자를 반환하고, 해당 인자를 삭제한다.
.clear() : 내부 데이터를 삭제하고 빈값으로 돌려준다.
.reverse() : 리스트를 거꾸로 정렬한다.
```

## 4. 오류의 종류

```
ZeroDivisionError : 0으로 나누었을때 발생하는 오류
NameError : namespace에 존재하지 않는 값을 사용했을때.
TypeError : type이 맞지않은 값을 사용하였을때
IndexError : 아직 할당되지않거나, 범위를 초과한 인덱스를 참조하려 했을때
KeyError : 존재하지 않는 Key값을 찾았을때 (.get()을 대체 사용)
ModuleNotFoundError : 정의되지 않은 모듈를 from 으로 가져오려 하였을때
ImportError : 모듈은 존재하지만, 정의되지않은 함수나 메서드를 import 하려했을때
```
