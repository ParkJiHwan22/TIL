# 08. Django - ORM_with_view

### 학습 목표

> Django View 함수를 사용하여 데이터베이스에서 가져온 데이터를 처리할 수 있는 능력을 가질 수 있다.

> Django ORM과 View 함수를 결합하여 웹 애플리케이션의 데이터를 저장하고 렌더링 할 수 있다.

# 1. 사전 준비

### app URLs 분할 및 연결

``` python
# articles/urls.py

from django.urls import path

app_name = 'articles'
urlpatterns = [
]
```

``` python
# crud/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  path('articles/', include('articles.urls')),
]
```


### index 페이지 작성

``` python
# articles/urls.py

from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
  path('', views.index, name='index'),
]
```

``` python
# articles/views.py

def index(request):
  return render(request, 'articles/index.html')
```

# 2. READ

### 전체 게시글 조회

### 단일 게시글 조회

# 3. CREATE

# Create 로직을 구현하기 위해 필요한 view 함수
- 사용자의 입력을 받는 페이지를 렌더링: `new`
- 사용자가 입력한 데이터를 받아 DB에 저장: `create`
