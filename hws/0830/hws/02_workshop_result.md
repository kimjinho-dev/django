1. intro/urls.py
   
```python
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lotto/', views.lotto),
]
```

2. pages/views.py

```python
from urllib import request
from django.shortcuts import render
import random
# Create your views here.
def lotto(request):
    context = {
        'lotto_num' : random.sample(range(1,46),6),
    }
    return render(request, 'lotto.html', context)
```

3. templates/lotto.html

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>lotto</title>
</head>

<body>
  <h1>제 394회 로또번호 추천</h1>
  <h2>SSAFY님께서 선택하신 로또 번호는 {{lotto_num}}입니다.</h2>
</body>

</html>
```