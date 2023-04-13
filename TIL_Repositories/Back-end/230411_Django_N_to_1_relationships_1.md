# 16. N_to_1_relationships_1

## 학습 목표

> django ForeignKey 필드를 사용하여 Many-to-one 관계를 만들 수 있다.

> Many-to-one 관계에서 역참조를 하는 방법을 이해하고 이를 데이터 조작에서 활용할 수 있다.

> Many-to-one 관계에서 관련된 객체를 추가, 수정 및 삭제할 수 있다.

# 1. 개요

### 관계형 데이터베이스의 N:1관계
- 주문 테이블의 `Foreign Key(외래키)`가 고객 테이블의 PK키가 됨

### Foreign Key
- 테이블의 필드 중 다른 테이블의 레코드를 식별할 수 있는 키
- 각 레코드에서 다른 테이블 간의 `관계`를 만드는 데 사용

# 2.1. Comment & Article - 모델 관계 설정

### Many to one relationships (N:1 or 1:N)
- 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 1개와 관련된 관계

### Comment(N) - Article(1)
- '0개 이상의 댓글은 1개의 게시글에 작성될 수 있다.'

### ForeignKey()
- django에서 N:1관계 설정 모델 필드

### Comment 모델 정의

``` python

class Comment(models.Model):
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  content = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
```

- ForeignKey()클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형(소문자)으로 작성하는 것을 권장
- ForeignKey 클래스를 작성하는 위치와 관계없이 필드 마지막에 생성됨

### ForeignKey(to, on_delete)
- to : 참조하는 모델 class 이름
- on_delete: 참조하는 모델 class가 삭제될 때 연결된 하위 객체의 동작을 결정

### on_delete
- 외래 키가 참조하는 객체(1)가 사라졌을 때, 외래 키를 가진 객체(N)를 어떻게 처리할 지를 정의하는 설정(데이터 무결성)

- 'CASCADE': 부모 객체(참조된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제

### Migration 진행 후 Comment 테이블 확인
- article_id 필드 확인
- 참조하는 클래스 이름의 소문자(단수형)로 작성하는 것이 권장되었던 이유

### 댓글 생성 연습하기
- shell_plus 실행 및 게시글 작성

> $ python manage.py shell_plus

``` python
# 게시글 생성
Article.objects.create(title='title', content='content')
```

- 댓글 생성

``` python
# 게시글 조회
article = Article.objects.get(pk=1)

# 외래 키 데이터 입력
comment.article = article
# 또는 comment.article_id = article.pk 처럼 pk 값을 직접 외래 키 컬럼에 넣어줄 수도 있지만 권장하지 않음

# DB에 댓글 저장 및 확인
comment.save()
```

- 댓글 생성 연습하기

``` python
comment.pk
=> 1

comment.content
=> 'first comment'

# 클래스 변수명인 article로 조회 시 해당 참조하는 게시물 객체를 조회할 수 있음
comment.article
=> <Article: Article object (1)>

# article_pk는 존재하지 않는 필드이기 때문에 사용 불가
comment.article_id
=> 1
```

- 댓글 생성

``` python
# 1번 댓글이 작성된 게시물의 pk 조회
comment.article.pk
=> 1

# 1번 댓글이 작성된 게시물의 content 조회
comment.article.content
=> 'content'
```

- 두번째 댓글 작성해보기

``` python
comment = Comment(content='second comment', article=article)
comment.save()

comment.pk
=> 2

comment
=> <Comment: Comment object (2)>

comment.article.pk
=> 1
```


# 2.2. Comment & Article - 관계 모델 참조

### 역참조
- 나를 참조하는 테이블(나를 외래 키로 지정한)을 참조하는 것
- N:1 관계에서는 1이 N을 참조하는 상황
- `하지만 Article에는 Comment를 참조할 필드가 없음`

### article.comment_set.all()
- 모델 인스턴스.related manager.Query API

### related manager
- N:1 or M:N 관계에서 역참조 시에 사용하는 manager
- objects라는 매니저를 통해 queryset api를 사용했던 것처럼 related manager를 통해 queryset api를 사용할 수 있게 됨

### related manager
- article.commnet 형식으로는 댓글 객체를 참조할 수 없음
- 실제 Article 클래스에는 Comment와의 어떠한 관계도 작성되어 있지 않기 때문
- 대신 Django가 역참조할 수 있는 'comment_set' manager를 자동으로 생성해 article.comment_set 형태로 댓글 객체를 참조할 수 있음
- N:1관계에서 생성되는 Related manager의 이름은 참조하는 `모델명_set`의 이름 규칙으로 만들어짐

### Related manager 연습하기
- shell_plus 실행 및 1번 게시글 조회

> $ python manage.py shell_plus

> article = Article.objects.get(pk=1)

- 1번 게시글에 작성된 모든 댓글 조회하기(역참조)

> article.comment_set.all()

- 1번 게시글에 작성된 모든 댓글 출력하기

``` python
comments = article.comment_set.all()
for comment in comments:
  print(comment.content)
```

## 2.3. Comment & Article - 댓글 기능 구현

### Comment CREATE
- 사용자로부터 댓글 데이터를 입력 받기 위한 CommentForm 작성

``` python
# articles/forms.py

from .models import Article, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
```

- detail 페이지에서 CommentForm 출력(view 함수)

``` python
# articles/views.py

from .forms import ArticleForm, CommentForm


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    # 해당 게시글에 작성된 모든 댓글을 조회(역참조)
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)
```

- detail 페이지에서 CommentForm 출력(템플릿)

``` html
<!-- articles/detail.html -->

<form action="{% url 'articles:comment_create' article.pk %}" method="POST">
  {% csrf_token %}
  {{ comment_form }}
  <input type="submit">
</form>
```

- 외래 키 필드는 `사용자의 입력으로 받는 것이 아니라 view 함수 내에서 받아 별도로 처리되어 저장`되어야 함

- detail 페이지에서 CommentForm 출력(템플릿)

``` python
# articles/forms.py

from .models import Article, Comment


class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('content',)
```

- 출력에서 제외된 외래 키 데이터는 어디서 받아와야 할까?

- detail 페이지의 url을 살펴보면 path('<int:pk>/', views.detail, name='detail') url에 해당 게시글의 pk 값이 사용되고 있음

- 댓글의 외래 키 데이터에 필요한 정보가 바로 게시글의 pk 값

- save(`commit=False`): DB에 저장하지 않고 인스턴스만 반환

``` python
# articles/views.py

def comment_create(request, review_pk):
    if request.method == "POST":
        review = Review.objects.get(pk=review_pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.user = request.user
            comment.save()
        return redirect('reviews:detail', review.pk)
    context = {
        'review': review,
        'comment_form': comment_form,
    }
    return render(request, 'reviews/detail.html', context)
```

### Comment READ

- 전체 댓글 출력(view 함수)

``` python
# articles/views.py

from .models import Review, Comment

def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    comment_form = CommentForm()
    comments = review.comment_set.all()
    context = {
        'review': review,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'reviews/detail.html', context)
```

- 전체 댓글 출력 (템플릿)

``` html
<!-- articles/detail.html -->
<h3>
  댓글 목록
</h3>
{% for comment in comments %}
  <div>
    <p>작성자 -
      {{ comment.user }}</p>
    <p>댓글 번호 -
      {{ comment.pk }}</p>
    <p>
      댓글 내용 -
      {{comment.content}}
    </p>
  </div>
  <hr>
{% endfor %}
```

### Comment DELETE

- 댓글 삭제 url 작성
- 댓글 삭제 view 함수 작성
- 댓글 삭제 버튼 작성

# 99. 참고

### 댓글 개수 출력하기
- DTL filter - length 사용

``` html
{{ comments|length }}

{{ article.comment_set.all|length }}
```

- QuerysetAPI - count() 사용
``` html
{{ article.comment_set.count }}
```

### 댓글이 없는 경우 대체 컨텐츠 출력

``` html
{{% empty %}}
  <p>댓글이 없어요...</p>
```

### 댓글 수정을 구현하지 않는 이유
- 일반적으로 댓글 수정은 수정 페이지로 이동 없이 현재 페이지가 유지된 상태로 댓글 Form 부분만 변경되어 수정할 수 있도록 함
- 이처럼 페이지의 일부 내용만 업데이트 하는 것은 JavaScript의 영역이기 때문에 JavaScript를 사용해 도전해 볼 수 있도록 함

### admin site 등록
- 새로 작성한 Comment 모델을 admin site에 등록하기

``` python
# articles/admin.py

from .models import Article, Comment


admin.site.register(Article)
admin.site.register(Comment)
```

