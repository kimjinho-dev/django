# 20220726 workshop

## 1. 무엇이 중복일까

```python
def duplicated_letters(words):
    duplicated_list = []
    for idx, word in enumerate(words):
        if idx == len(words):
            break
        if words[idx + 1 :].find(word) != -1 and duplicated_list.count(word) == 0:
            duplicated_list.append(word)
    return duplicated_list
```

## 2. 소대소대

```python
def low_and_up(words):
    new_word = ''
    for idx, word in enumerate(words):
        if idx % 2 == 0:
            new_word += word.lower()
        else:
            new_word += words[idx].upper()
    return new_word
```

```python
# 한줄표현
def low_and_up(word):
    new_str = [char.upper() if idx%2 else char.lower() for idx, char in enumerate(word)]
    return ''.join(new_str)
```

## 3. 솔로천국 만들기

```python
def lonely(num_list):
    solo_heaven = [num_list[0]]
    for idx, num in enumerate(num_list):
        if num != solo_heaven[-1]:
            solo_heaven.append(num)

    return solo_heaven
```