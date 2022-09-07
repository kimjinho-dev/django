# 0725 homework

## 1. 모음은 몇개나 있을까?

```python
def count_vowels(word):
    # vowels = ['a', 'e', 'i', 'o', 'u']
    vowels = 'aeiou'
    count = 0
    for vowel in vowels:
        count += word.count(vowel)
    return count
```

## 2. 문자열 조작

다음 중 문자열을 조작하는 방법으로 옳지 않은것을 고르시오 

```
(1) .find(x)는 x의 첫번째 위치를 반환한다. 없으면 -1을 반환한다.
(2) .split([chars])은 특정 문자를 지정하면 문자열을 특정 문자를
기준으로 나누어 list로 반환한다.
특정 문자를 지정하지 않으면 공백을 기준으로 나눈다.
(3) .replace(old, new[, count])는 바꿀 대상 문자를 새로운 문자로
바꿔서 반환한다.
(4) .strip([chars])은 특정 문자를 지정하면, 양쪽에서 해당 문자를
찾아 제거한다. 특정 문자를 지정하지 않으면 오류가 발생한다.
```

```
정답 : (4) 문자를 지정하지않으면, 공백을 제거한다.
```


## 3. 정사각형만 만들기

```python
def only_square_area(widths, hights):
    sqare = []
    for width in widths:
        if hights.count(width) != 0:
            sqare.append(width * width)
    return sqare
```