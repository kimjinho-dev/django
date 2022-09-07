# 1. 각 문항을 읽고 맞으면 T, 틀리면 F를 작성하시오.

##### (1) ModelForm을 사용할 때 Meta 클래스의 model 변수는 반드시 작성해야 한다.
: T  
-> 참조하는 모델을 알아야하기때문에 필요하다

##### (2) ModelForm을 사용할 때 사용자의 입력을 위해 페이지에 렌더링 되는 input element의 속성은 Django에서 제공 해주는 대로만 사용해야 한다.
: F
=> widget 속성을 통하여 input태그처럼 원하는 대로 설정할 수 있다.


##### (3) 화면에 나타나는 각 element 위치는 html에서 form.as_p()를 사용하지 않고,직접 위치시킬 수 있다.
: F
=> 모델폼에서 element의 위치는 단순히 한줄로 나열하듯이 표현된다. 이를 별도로 개행을 나눌수는 없고, as_p나 다른 식을 사용해서 위치시켜야한다.

# 2. 다음 빈칸 (a) ~ (d) 에 적합한 코드를 작성하시오.

```python
from django import (a)forms
from .models import Article

class ArticleForm((b)forms.ModelForm):
  class Meta:
    model = (c)Article
    (d)fields = '__all__'

```
(a) = forms 
(b) = forms.ModelForm
(c) = Article
(d) = fields

