# 20220719 homework_기초문법과 데이터 타입

## 1. Mutable & Immutable

```
mutable은 리스트, 세트, 딕셔너리 형식이 있고
immutable은 레인지, 듀플 형식이 있다.
따라서 
Mutable = list , set , dictinary
immutable = string , Tuple , range
```

## 2. Dictionary 만들기

```python
dict_class = {'kim' : 23 , 'min' : 25 , 'song' : 26}
```

## 3. 평균 구하기

```python
scores = [80,89,99,83]
sum = 0
for x in scores:
  sum += x

print(sum/len(scores))
```