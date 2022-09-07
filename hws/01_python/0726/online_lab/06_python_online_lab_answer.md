### 06_python_online_lab



**데일리 과제 6-2 답안 및 해설**

```python
# mass percent.py

salt = []  # 소금
salt_water = []  # 소금물
i = 0

while i < 5:
    i += 1
    s = input(f'{i}.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: ')

    if s == 'Done':
        break

    S, L = int(s[: s.find('%')]), int(s[s.find(' ') + 1 : s.find('g')])

    salt.append(S * L / 100)
    salt_water.append(L)

print('{:.2f}% {}g'.format(sum(salt) / sum(salt_water) * 100, sum(salt_water)))

```

- while 문의 조건을 통해 5번 내로 반복하도록 한다.

- S, L 을 튜플 대입을 통해 할당한다.
  - `s[:s.find("%")]`: 퍼센트%의 인덱스를 찾아서 그 이전까지 슬라이싱한다.
  - `s[s.find(" ")+1:s.find("g")]` : 빈칸의 인덱스+1부터 문자 g의 인덱스까지 슬라이싱한다.
  - 각각 슬라이싱된 문자열을 `int` 함수를 통해 숫자로 바꾸어 할당한다.

- **농도 \* 물 / 100 = 소금** 이므로, `salt`에 `S * L / 100`를 `append`해준다.

- 이렇게 구한 소금과 소금물의 리스트를 가지고 다시 농도를 구한다.

  - 소금물의 농도는 `소금 / 물 * 100` 으로 계산하여 출력한다.