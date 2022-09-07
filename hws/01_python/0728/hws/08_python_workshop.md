# 20220728 workshop

## 1. 도형 만들기

### point

```python
class Point:
  def __init__(self, x, y):
      self.x = x
      self.y = y


class Rectangle:
  def __init__(self, p1, p2):
      self.p1x = p1.x
      self.p1y = p1.y
      self.p2x = p2.x
      self.p2y = p2.y
    #   self.x = x 
    #   self.y = y 

  def get_area(self):
      return abs((self.p1x - self.p2x) * (self.p1y - self.p2y))

  def get_perimeter(self):
      return (abs((self.p1x - self.p2x)) + abs((self.p1y - self.p2y))) * 2

  def is_square(self):
      return abs((self.p1x - self.p2x)) == abs((self.p1y - self.p2y))

"""
class Rectangle:
  def __init__(self, p1, p2):
      self.p1 = [p1.x, p1.y]
      self.p2 = [p2.x, p2.y]

  def get_area(self):
      return abs((self.p1[0] - self.p2[0]) * (self.p1[1] - self.p2[1]))

  def get_perimeter(self):
      return abs((self.p1[0] - self.p2[0])) + abs((self.p1[1] - self.p2[1])) * 2

  def is_square(self):
      return abs((self.p1[0] - self.p2[0])) == abs((self.p1[1] - self.p2[1]))
"""

```
