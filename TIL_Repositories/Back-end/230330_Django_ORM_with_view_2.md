# 09. Django - ORM with view

## 학습 목표

> HTTP request methods를 사용해 클라이언트가 서버로 보내는 요청의 종류를 나타낼 수 있다.

> HTTP response status codes를 사용해 서버가 클라이언트에 반환하는 응답의 상태를 올바르게 나타낼 수 있다.

> Django View 함수를 사용하여 데이터베이스에서 가져온 데이터를 삭제 및 수정할 수 있다.

# 1. HTTP request methods

### HTTP request methods
- 게시글 작성 후 작성 완료를 나타내는 페이지를 렌더링 하는 것
- 게시글을 "조회해줘!" 라는 요청이 아닌 "작성해줘!"라는 요청이기 때문에 페이지 렌더링은 적절한 응답이 아님
- `데이터 저장 후 유저를 어디론가 다시 보내야 함`

### redirect()
- 인자에 작성된 주소로 다시 요청을 보냄

``` Python
from django.shortcuts import render, redirect

def create(request):
  title = request.GET.get('title')
  content = request.GET.get('content')
  article = Ariticle(title=title, content=content)
  article.save()

  return redirect('articles:detail', article.pk)
```

- create view: 함수 수정
- redirect: 함수 적용

### HTTP
- 네트워크 상에서 데이터를 주고 받기위한 약속

### HTTP request methods
- 데이터(리소스)에 어떤 요청(행동)을 원하는지를 나타내는 것
- `GET`&`POST`

### 'GET' Method
- 특정 리소스를 조회하는 요청
- GET으로 데이터를 전달하면 Query String 형식으로 보내짐
- `반드시 데이터를 가져올 때만 사용해야 함`

### 'POST' Method
- 특정 리소스에 변경사항을 만드는 요청
- POST로 데이터를 전달하면 HTTP Body에 담겨 보내짐

### HTTP response status code
- 특정 HTTP 요청이 성공적으로 완료되었는지 알려줌
- 5개의 그룹으로 나뉘어짐(1xx, 2xx, 3xx, 4xx, 5xx)

### 403 Forbidden
- 서버에 요청이 전달되었지만, 권한 때문에 거절되었다는 것을 의미

### CSRF(Cross-Site-Request-Forgery)
- "사이트 간 요청 위조"
- 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹 페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법

### Security Token (CSRF Token)
- "대표적인 CSRF방어 방법"
1. 서버는 사용자 입력 데이터에 임의의 난수 값(token)을 부여
2. 매 요청마다 해당 token을 포함시켜 전송 시키도록 함
3. 이후 서버에서 요청을 받을 때마다 전달된 token이 유효한지 검증

``` HTML
{% csrf_token %}
```

- DTL의 `csrf_token 태그`를 사용해 사용자에게 토큰 값을 부여
- 요청 시 토큰 값도 함께 서버로 전송될 수 있도록 함

#### POST Method는 데이터 베이스에 대한 변경사항을 만드는 요청이기 때문에 토큰을 사용해 최소한의 신원 확인을 하는 것

# 2. Delete

### Delete 로직 작성

``` Python
# articles/urls.py

app_name = 'articles'
urlpatterns = [
  path('<int:artilce_pk>/delete/', views.delete, name='delete'),
]

# articles/views.py

def delete(request, artilce_pk):
  article = Article.objects.get(pk=article_pk)
  article.delete()
  return redirect('articles:index')
```

``` HTML
<form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="삭제">
  </form>
```


# 3. Update

### Update 로직을 구현하기 위해 필요한 view 함수
- 사용자의 입력을 받는 페이지를 렌더링: `edit`
- 사용자가 입력한 데이터를 받아 DB에 저장: `update`

### edit 로직 작성

``` Python
# articles/urls.py

app_name = 'articles'
urlpatterns = [
# 데이터 수정 페이지에 대한 URL 패턴
  path('<int:article_pk>/edit/', views.edit, name='edit'),
]

# articles/views.py

def edit(request, article_pk):
  article = Article.objects.get(pk=article_pk)
  context = {
      'article': article
  }
  return render(request, 'articles/edit.html', context)
```

``` HTML
<form action="{% url 'articles:update' article.pk %}" method="POST">
  {% csrf_token %}
  <div>
    <label for="title">제목: </label>
    <input type="text" name="title" id="title" value="{{ article.title }}">
  </div>
  <div>
    <label for="content">내용: </label>
    <textarea name="content" id="content" cols="30" rows="10">{{ article.content }}</textarea>
  </div>
  <input type="submit" value="[UPDATE]">
</form>
```

- `수정 시 이전 데이터가 출력될 수 있도록 처리`

### update 로직 작성

``` Python
# articles/urls.py

app_name = 'articles'
urlpatterns = [
  path('<int:article_pk>/update/', views.update, name='update'),
]

# articles/views.py

def update(request, article_pk):
  article = Article.objects.get(pk=article_pk)
  article.title = request.POST.get('title')
  article.content = request.POST.get('content')
  article.save()
  return redirect('articles:detail', article.pk)
```

``` HTML
<form action="{% url 'articles:create' %}" method="POST">
  {% csrf_token %}
  <div>
    <label for="title">제목: </label>
    <input type="text" name="title" id="title">
  </div>
  <div>
    <label for="content">내용: </label>
    <textarea name="content" id="content" cols="30" rows="10"></textarea>
  </div>
  <input type="submit">
</form>
<a href="{% url 'articles:index' %}">[back]</a>
```
