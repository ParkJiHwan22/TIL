# 15. Django - Static_files

## 학습 목표

> Django에서 Static files를 처리하는 방법과 동작 방식을 이해하고, templates에서 Static files을 사용할 수 있다.

> media file의 특징과 활용 방법을 숙지하고 올바른 경로에 이미지 파일을 업로드해 사용자에게 제공할 수 있다.

# 0. Static files를 사용하는 이유

- Static files는 웹 애플리케이션에서 정적인 콘텐츠를 제공하는데 사용됨

- HTML, CSS, JavaScript, 이미지 파일 등을 포함하며, 웹 페이지의 외관과 기능을 결정하는 데 필수적

- 웹 애플리케이션에서 모든 내용을 동적으로 생성한다면 서버에 부하가 많이 걸리게 되고, 클라이언트 측에서 매번 새로운 데이터를 받아와야 하기 때문에 성능이 저하될 수 있음

- Static files를 사용하면, 이러한 파일들은 브라우저에 캐싱되어 클라이언트가 이전에 다운로드한 파일을 사용할 수 있으므로, 서버에 부하가 줄어들고, 웹 페이지가 더 빠르게 로드되어 사용자 경험을 향상시킬 수 있음

# 1. 개요

### Static Files
- 서버 측에서 변경되지 않고 고정적으로 제공되는 파일
- 이미지, JS, CSS 파일 등

### 웹 서버와 정적 파일
- 웹 서버의 기본동작은 특정 위치(URL)에 있는 자원을 요청(HTTP request)받아서 응답(HTTP response)을 처리하고 제공(serving)하는 것
- 웹 서버는 요청 받은 URL로 서버에 존재하는 정적 자원(static resource)을 제공함
- `정적 파일을 제공하기 위한 경로(URL)가 있어야 함`

# 2. Static files 제공하기

### 경로에 따른 Static file 제공하기
- 기본 경로 : app/static/
- 추가 경로 : STATICFILES_DIRS

### 기본 경로 static file 제공하기
- articles/static/articles/경로에 이미지 파일 배치
- static tag를 사용해 이미지 파일에 대한 url 제공

``` html
<!-- articles/index.html -->

{% load static %}

<img src="{% static 'articles/sample-1.png' %}" alt="img">
```

### STATIC_URL
- 기본 경로 및 추가 경로에 위치한 정적 파일을 참조하기 위한 URL
- 실제 파일이나 디렉토리가 아니며, URL로만 존재

- `비어 있지 않은 값으로 설정한다면 반드시 slash(/)로 끝나야 함`

``` python
# settings.py

STATIC_URL = '/static/'
```

- URL + STATIC_URL + 정작파일 경로


### 추가 경로 static file 제공하기
- 추가 경로에 이미지 파일 배치

``` python
### settings.py

STATICFILES_DIRS = [
  BASE_DIR / 'static',
]
```

- static tag를 사용해 이미지 파일에 대한 url 제공

``` html
<!-- articles/index.html -->

<img src="{% static 'sample-2.png' %}" alt="img">
```

### STATICFILES_DIRS
- 정적 파일의 기본 경로 외에 추가적인 경로 목록을 정의하는 리스트

# 3. Media Files
- 사용자가 웹에서 업로드하는 정적 파일(user-uploaded)

### ImageField()
- 이미지 업로드에 사용하는 모델 필드
- `이미지 객체가 직접 저장되는 것이 아닌 '이미지 파일의 경로 문자열'이 DB에 저장`

### 미디어 파일을 제공하기 전 준비
1. settings.py에 MEDIA_ROOT, MEDIA_URL 설정
2. 작성한 MEDIA_ROOT와 MEDIA_URL에 대한 url지정

### MEDIA_ROOT
- 미디어 파일들이 위치하는 디렉토리의 절대 경로

``` python
# settings.py

MEDIA_ROOT = BASE_DIR / 'media'
```

### MEDIA_URL
- MEDIA_ROOT에서 제공되는 미디어 파일에 대한 주소를 생성(STATIC_URL과 동일한 역할)

``` python
### settings.py

MEDIA_URL = [ '/static/']
```

### MEDIA_ROOT와 MEDIA_URL에 대한 url 지정

``` python
# crud/urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

- 업로드 된 파일의 URL == settings.MEDIA_URL
- 위 URL을 통해 참조하는 파일의 실제 위치 == settings.MEDIA_ROOT

# 4. 이미지 업로드 및 제공하기

### 이미지 업로드

#### 1. blank=True 속성을 작성해 빈 문자열이 저장될 수 있도록 설정

``` python
# articles/models.py
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d')
```

#### 2. migration 진행

> pip install pillow

> pip freeze > requirements.txt

#### 3. form 요소의 enctype 속성 추가

``` html
<!-- articles/create.html -->

 <h1>Create</h1>
  <form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data">
```

#### 4. view 함수에서 업로드 파일에 대한 추가 코드 작성

``` python
# articles/views.py

def create(request):
    if request.method == 'POST':
        # print(request.FILES)
        form = ArticleForm(request.POST, request.FILES)
```

- 파일 자체가 아닌 "경로"가 저장되는 것

### 업로드 이미지 제공하기

#### 1. url 속성을 통해 업로드 파일의 경로 값을 얻을 수 있음
- url 속성을 통해 업로드 파일의 경로 값을 얻을 수 있음

``` html
<!-- articles/detail.html -->
  <img src="{{ article.image.url }}" alt="IMAGE">
```

- article.image.url - 업로드 파일의 경로
- article.image - 업로드 파일의 파일 이름

#### 2. 업로드 출력 확인 및 MEDIA_URL 확인

#### 3. 업로드 이미지 제공하기
- 이미지를 업로드하지 않은 게시물은 detail 템플릿을 출력할 수 없는 문제 해결
- 이미지 데이터가 있는 경우만 이미지를 출력할 수 있도록 처리

``` html
<!-- articles/detail.html -->
  {% if article.image %}
    <img src="{{ article.image.url }}" alt="IMAGE">
  {% endif %}
```

### 업로드 이미지 수정

#### 1. 수정 페이지 form 요소에 enctype 속성 추가

``` html
<!-- articles/update.html -->

  <h1>Update</h1>
  <form action="{% url 'articles:update' article.pk %}" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="UPDATE">
  </form>
```

#### 2. view 함수에서 업로드 파일에 대한 추가 코드 작성

``` python
# articles/views.py

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
```

# 99. 참고

### 'upload_to' argument
- ImageField()의 upload_to 인자를 사용해 미디어 파일 추가 경로 설정

``` python
# 1
image = models.ImageField(blank=Ture, upload_to='images/')

# 2
image = models.ImageField(blank=Ture, upload_to='%Y/%m/%d/')

# 3
def articles_image_path(instance, filename):
    return f'images/{instance.user.username}/{filename}'

image = models.ImageField(blank=Ture, upload_to=articles_image_path)
```
