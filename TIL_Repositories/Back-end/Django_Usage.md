# **` 1. 개발 환경 설정 가이드 작성`**
- 아래 일련의 Django 개발 환경 설정 및 서버 실행 과정에 대한 본인만의 가이드 작성

## 1. 가상환경 생성(가상환경 이름 : venv)

> $ python -m venv venv

### 1.1 가상환경 설정 확인

> pip list

## 2. 가상환경 활성화

> $ source venv/Scripts/activate

## 3. django 설치
- 설치 버전 : 3.2.18 (현 LTS)

> $ pip install django==3.2.18

## 4. 의존성 파일 requirements.txt 생성

> $ pip freeze > requirements.txt

## 5. django 프로젝트 생성

> $ django-admin startproject firstpjt .

## 6. django 서버 실행
- 로켓 발사 화면 확인

> $ python manage.py runserver

### 6.1 VSC에서 환경설정
- ctrl + shift + p
- interpreter 라고 검색하고 Python: Select Interpreter 선택
- venv 선택하기

## 7 .gitignore 파일 만들기
- gitignore 파일 생성
- gitignore.io 사이트로 들어가서 windows, macOS, VisualStudioCode, python, django 를 선택하고 생성
- gitignore 파일에 붙여넣기

## 8 git 초기화

> $ .git init

#### 8.1 .git status로 확인
- venv 가 제외되었는지 확인(db도 제외됨)

> $ git status 

## 9. git add . 하고 commit해서 서버에 올리기
- github에 원격저장소 생성
- remote 연결
- push


# **`2. 파일을 받는 팀원 입장`**

## 1. 가상환경 생성(가상환경 이름 : venv)

> $ python -m venv venv

## 1.1 가상환경 설정 확인

> $ pip list

## 2. 파일 공유받기

> $ pip install -r reqirements.txt


# **`3. django 디자인 패턴`**

## 1. 앱 생성

> $ python manage.py startapp articles

## 2. 앱 등록

``` python
INSTALLED APPS = [
  'articles', # 앱 이름 추가
  'django.contrib.admin',
  'django.contrib.auth',
  ...
]
```

## 3. URLs 설정

``` python
# urls.py

from django.contrib import admin
from django.urls import path
from articles import views # articles 패키지에서 views 모듈을 가져옴

urlpatterns = [
  path('admin/', admin.site.urls),
  path('articles/', views.index), # articles/로 요청이 오면 `views` 모듈의 `index`뷰 함수를 호출
]
```

## 4. View

``` python
def index(request):
  return render(request, 'articles/index.html')
```

- 특정 경로에 있는 template과 request 객체를 결합해 응답 객체를 반환하는 index view 함수 정의

## 5. Template
- articles 앱 폴더 안에 templates 폴더 작성
- templates 폴더 안에 템플릿 페이지 작성

# **`4. Django Template Language(DTL)`**
- Template에서 조건, 반복, 변수, 필터 등의 프로그래밍적 기능을 제공하는 시스템

## 1. Variable
- view 함수에서 render 함수의 세번째 인자로 딕셔너리 타입으로 넘겨받을 수 있음
- 딕셔너리 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
- dot(.)를 사용하여 변수 속성에 접근 할 수 있음

``` python
{{ variable }}
```

## 2. Filters
- 표시할 변수를 수정할 때 사용
- chained가 가능하며 일부 필터는 인자를 받기도 함
- 약 60개의 built-in template filters를 제공

``` python
{{ variable|filter }}
```

## 3. Tags
- 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
- 일부 태그는 시작과 종료 태그가 필요
- 약 24개의 built-in template tags를 제공

``` python
{{% tag %}}
```

## 4. Comments
- DTL에서의 주석 표현

``` JavaScript
<h1>Hello, {# name #}</h1>
```

# **`5. 템플릿 상속`**
- 페이지의 공통 요소를 포함하고, 하위 템플릿이 재정의 할 수 있는 공간을 정의하는 기본 'skeleton'템플릿을 작성하여 상속 구조를 구축

## 1. 'extends' tag

``` JavaScript
{% extends 'path' %}
```

- 자식(하위)템플릿이 부모 템플릿을 확장한다는 것을 알림
- `반드시 템플릿 최상단에 작성되어야 함(2개 이상 사용 불가)`

## 2. 'block' tag

``` JavaScript
{% block name %}{% endblock name %}
```

- 하위 템플릿에서 재정의(overridden)할 수 있는 블록을 정의
- 하위 템플릿이 작성할 수 있는 공간을 지정

# **`6. 요청과 응답`**

``` HTML
<form action="{% url 'articles:update' article.pk %}" method="POST">
  <div>
    <label for="title">제목: </label>
    <input type="text" name="title" id="title" value="{{ article.title }}">
  </div>
</form>
```
## 1. 'form' element
- 사용자로부터 할당된 데이터를 서버로 전송
- 웹에서 사용자 정보를 입력하는 여러 방식(text, password 등)을 제공

## 2. action
- 입력 데이터가 전송될 URL을 지정(목적지)
- 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐

## 3. method
- 데이터를 어떤 방식으로 보낼 것인지 정의
- 데이터의 HTTP request methods(GET, POST)를 지정

## 4. 'input' element
- 사용자의 데이터를 입력 받을 수 있는 요소
- type 속성 값에 따라 다양한 유형의 입력 데이터를 받음

## 5. 'name'
- input의 핵심 속성
- 데이터를 제출했을 때 name 속성에 설정된 값을 통해 사용자가 입력한 데이터에 접근할 수 있음

# **`7. 변수, APP의 URL`**

## 1. Variable Routing
- URL 일부에 변수를 포함시키는 것
- 변수는 view 함수의 인자로 전달할 수 있음

``` Python
path('articles/<int:num>/', views.hello),
path('hello/<str:name>/', views.greeting),
```

## 2. Path converters
- URL 변수의 타입을 지정
- str, int 등 5가지 타입 지원

## 3. APP의 URL
- 각 앱에 URL을 정의하는 것
- 프로젝트와 각각의 앱이 URL을 나누어 관리하여 주소를 관리하기 편하게 하기 위함

``` Python
# crud/urls.py

from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  # path('articles/', include('articles.urls')),
  # path('pages/', include('pages.urls')),
  ...
]
```

## 4. URL 이름 지정(Naming URL patterns)
- URL에 이름을 지정하는 것

``` python
# articles/urls.py

path('index/', view.index, name='index'),
```

## 5. 'url' tag
- 주어진 URL 패턴의 이름과 일치하는 절대 경로 주소를 반환

``` python
{% url 'url-name' arg1 arg2 %}
```

## 6. app_name 속성 지정

``` python
# articles/ulrs.py

app_name = 'articles'
urlpatterns = [
  ...,
]
```

## 7. URL tag의 변화

``` python
{% url 'articles:index' %}
```

# **`8. model 클래스 작성`**

## 1. model 클래스 작성

``` python
# articles/models.py

class Article(models.Model):
  title = models.CharField(max_length=10)
  content = models.TextField()
```

## 2. makemigrations
- model class를 기반으로 설계도(migration)작성

> $ python manage.py makemigrations

## 3. migrate
- 만들어진 설계도를 DB에 전달하여 반영

> $ python manage.py makemigrations

## 4. admin 계정 생성

> $ python manage.py createsuperuser

## 5. admin에 모델 클래스 등록

``` python
# articles/admin.py

from django.contrib import admin
from .models import Article

admin.site.register(Article)
```

- admin.py에 등록하지 않으면 admin.site에서 확인할 수 없음

# **`9. Django-ORM`**

- Object-Relational-Mapping

## 1. QuerySetAPI 구문

> Article.objects.all()

- Model class, Manager, Queryset API