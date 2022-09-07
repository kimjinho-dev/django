# 20220802 homework

## 1.semantic Tag

```
시맨틱 태그는 header,section,footer이다.
나머지는 기본 html 내장 태그이다.
```

## 2. input Tag

```html
<div>
  <label for="username">USERNAME :</label>
  <input type="text" id="username" placeholder="아이디를 입력 해 주세요.">
</div>

<div>
  <label for="pwd">PWD :</label>
  <input type="text" id="pwd">
  <input type="button" value="로그인">
</div>
```

## 3. 크기 단위

```
rem. rm과 다르게 기존 HTML의 요소 기준 사이즈이다.
```

## 4. 선택자

```
div > p 는 자식 결합자로, 같은 범위내에서만 작용한다.
div p 는 자손 결합자는 하위 범위에서도 작용한다.

<div>
  <p>자식</p>
  <ul>
    <p>자손</p>
  </ul>
</div>

위와같은 코드에서 자식은 div의 자식이면서 자손이기때문에 2가지 속성을 모두 적용되지만
자손은 div의 자손이기때문에 div p 속성만 적용된다.
```