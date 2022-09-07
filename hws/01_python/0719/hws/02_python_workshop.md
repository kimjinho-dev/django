# 20220719 workshop_기초문법과 데이터 타입


## 1. 숫자의 입력과 출력

```python
first = int(input())
second = int(input())
print(first+second)
```

## 2. Dictionary를 활용하여 평균 구하기

```python
dict_lunch = {'ramen' : 5000 , 'row fish' : 10000}
total = 0
list_of_key = list(dict_lunch.keys())

for menu in list_of_key:
    total += dict_lunch[menu]

print(total / len(list_of_key))
```