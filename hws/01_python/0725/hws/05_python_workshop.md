# 0725 workshop

## 1. 평균점수 구하기

```python
def get_dict_avg(dict):
    values_list = dict.values()
    return sum(values_list) / len(values_list)
```

## 2. 혈액형 분류하기

다음 중 문자열을 조작하는 방법으로 옳지 않은것을 고르시오 

```python
def count_blood(blood_list):
    dict_blood = {}
    bloods = ['A', 'B', 'O', 'AB']
    for blood in bloods:
        dict_blood[blood] = blood_list.count(blood)
    # dict_blood.update(A=bloods.count('A'))
    # dict_blood.update(B=bloods.count('B'))
    # dict_blood.update(O=bloods.count('O'))
    # dict_blood.update(AB=bloods.count('AB'))
    return dict_blood
```