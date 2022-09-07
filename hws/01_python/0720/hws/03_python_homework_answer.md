### 03_python_homework.md

1. Built-in 함수

   Python에서 기본으로 사용할 수 있는 built-in 함수를 최소 5가지 이상 작성하시오.

   `abs()` `all()` `any()` `ascii()` `bool()` `bytes()`

   
   
2. 홀수만 담기

   * range와 slicing을 활용하여 1부터 50까지 숫자 중 홀수로 이루어진 리스트를 만드시오.

     ```python
     a = list(range(1, 51))
     b = a[0:-1:2]
     print(b)
     b = a[::2]
     # print(a)
     print(b)
     ```
   
   
   
2. 반복문으로 네모 출력

   * 두 개의 정수 n과 m이 주어졌을 때, 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 별(*) 문자를 이용하여 출력하시오.

   * 단, 반복문을 사용하여 작성하시오.
   
     ```python
     for height in range(m):
         for width in range(n):
             print('*', end='')
         print()
     ```
   
   
   
2. 조건 표현식

   - 제시된 if 문을 조건 표현식으로 바꾸어 작성하시오.

     ```python
     temp = 36.5
     print('입실 불가') if temp >= 37.5 else print('입실 가능')
   
   
   
5. 정중앙 문자

   문자열을 전달 받아 해당 문자열의 정중앙 문자를 반환하는 get_middle_char 함수를 작성하시오. 단, 문자열의 길이가 짝수일 경우에는 정중앙 문자 2개를 반환한다.

   ```python
   get_middle_char('ssafy')  # => a
   get_middle_char('coding')  # => di
   ```

   ```python
   def get_middle_char(word):
       num = len(word) // 2
   
       # 코드
       if len(word) % 2:
           middle = word[num]
       else:
           middle = word[num - 1 : num + 1]
   
       return middle
   ```

