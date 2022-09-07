# 20220728 homework

## 1. Circle 인스턴스 만들기

```python
class Circle:
  pi = 3.14
  def __init__(self,r,x,y):
    self.r = r
    self.x = x
    self.y = y

  def area(self):
    return Circle.pi * self.r * self.r

  def circumference(self):
    return 2 * Circle.pi * self.r

  def center(self):
    return (self.x, self.y)

circle1 = Circle(3,2,4)
print(circle1.area())
print(circle1.circumference())
```

## 2. Dog과 Bird는 Animal이다

```python
class Dog(Animal):
    # def __init__(self, name):
    #     super().__init__(name)    # 생략가능

    def run(self):
        print(f'{self.name}! 달린다!')

    def bark(self):
        print(f'{self.name}! 짖는다!')


class Bird(Animal):
    # def __init__(self, name):
    #     super().__init__(name)    # 생략가능

    def fly(self):
        print(f'{self.name}! 푸드덕!')

    # def walk(self):
    #     super().walk()            # 생략가능
```

## 3. Module Import

```python
from fibo import fibo_recursion as recursion
```