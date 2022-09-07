### 07_python_online_lab



**데일리 과제 7-2 답안 및 해설**

```python
class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1

    def __del__(self):
        Doggy.num_of_dogs -= 1

    def bark(self):
        return '왈왈!'

    @classmethod
    def get_status(cls):
        return f'Birth: {cls.birth_of_dogs}, Current: {cls.num_of_dogs}'

```

- `__init__` : 생성자
   - 개는 초기화 메서드에서 인자로 이름 name과 견종 breed을 받아서 인스턴스 변수에 할당한다.
   
- `__del__` : 소멸자
   - 개가 죽는 경우 `num_of_dogs`를 -1 하여 할당한다.
   
- `get_status` : 클래스 메서드로, 클래스 변수인 `birth_of_dogs`와 `num_of_dogs`을 사용한 문자열을 return한다.