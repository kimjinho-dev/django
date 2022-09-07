# 20220727 workshop
## 1. pip

```
(1) 해당 코드는 faker이라는 패키지를 설치하게 한다.
(2) git bash와 같은 리눅스 환경 터미널에서 실행시켜야한다.
```

## 2. Basic Usages

```python
from faker import Faker     # 1 faker 라이브러리를 가져오기 위한 을 하기 위한 코드이다.
fake = Faker()              # 2 Faker는 클래스, fake는 인스턴트 변수이다.
fake.name()                 # 3 name()은 fake의 인스턴트 메서드이다.
```

## 3. Localization

```python
class Faker():

    def __init__(self,name):
        pass
```

## 4. Seeding the Generator

①
```python
fake1 = Faker('ko_KR')
Faker.seed(87654321)
print(fake1.name())         # 1 이진호 (고정)
fake2 = Faker('ko_KR')
print(fake2.name())         # 2 강은주 (고정)
```

`클래스 메서드`
: 클래스.메서드 형태로 클래스 메서드이다.
추가로 seed() 한번으로 faker1,faker2 두 인스턴트 변수값이 고정된것으로 보아
클래스 변수값을 변경한것으로 보인다.

②
```python
fake1 = Faker('ko_KR')
fake1.seed_instance(87654321)
print(fake1.name())         # 1 이진호 (고정)
fake2 = Faker('ko_KR')
print(fake2.name())         # 2 진영호 (가변)
```

`인스턴트 메서드`
: 인스턴트.메서드 형태로 인스턴트 메서드이다.
추가로 seed_instance()로 시드값을 넣어준 fake1 인스턴트만 변하지 않는것으로 보아
클래스 변수값을 변경한것이 아니라 인스턴트 변수값을 변경한것으로 보인다.