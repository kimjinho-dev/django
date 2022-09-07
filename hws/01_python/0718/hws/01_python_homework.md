# 20220718 homework

## 1. pythone 예약어

```
list , int , def , True , False , and , else , elif , if , or , in , not , break , for , while

```

## 2. 실수비교

```python
num1 = 0.1 * 3
num2 = 0.3
print(abs(num1-num2) <= 1e-10)
```

## 3. 이스케이프 시퀀스

```python
print('\n')
print('\t')
print('\\')
```

## 4. string interpolation

```python
name = '철수'
a = '안녕, '
b = '야'
print(a+name+b)
```

## 5. 형변환

```python
int('3.5') # (5)번
```

## 6. 네모 출력

```python
n = 5
m = 9
squar = '*' * n + '\n'
squar *= m
print(squar) 
```

## 7. 이스케이프 시퀀스 응용

```python
print('"파일은 c:\\Windows\\Users\\내문서\\Python에 저장이 되었습니다."\n나는 생각했다. \'cd를 써서 git bash로 들어가 봐야지.\'')
```

## 8. 근의 공식

```python
a = 1       
b = -2
c = -3      # 이차방정식 예시

quadratic = ( -b + (((b**2)-4*a*c)**(1/2)) ) / (2*a) , ( -b - (((b**2)-4*a*c)**(1/2)) ) / (2*a)

print(quadratic)
```