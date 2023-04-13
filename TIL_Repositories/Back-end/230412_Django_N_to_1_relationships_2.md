# 17. N_to_1_relationships_2

# 학습 목표

> django ForeignKey 필드를 사용하여 Many-to-One 관계를 만들 수 있다.

> Many-to-one 관계에서 역참조를 하는 방법을 이해하고 이를 데이터 조작에서 활용할 수 있다.

> Many-to-one 관계에서 관련된 객체를 추가, 수정 및 삭제할 수 있다.

# 1. 개요

### Article(N) - User(1)
- 0개 이상의 게시글은 1개의 회원에 의해 작성될 수 있음

### Comment(N) - User(1)
- 0개 이상의 댓글은 1개의 회원에 의해 작성될 수 있음

# 2.1. Article & User - 모델 관계 설정


#### User 외래 키 정의

``` python
# articles/models.py

from django.conf import settings

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

### User 모델을 참조하는 2가지 방법
- get_user_model(), 반환 값: 'User Object'(객체)
  - `models.py가 아닌 다른 모든 곳에서 참조할 때 사용`
- settings.AUTH_USER_MODEL, 반환 값: 'accounts.User'(문자열)
  - `models.py의 모델 필드에서 참조할 때 사용`

  ### Migration 진행
  - 기본적으로 모든 컬럼은 NOT NULL 제약조건이 있기 때문에 데이터가 없이는 새로 추가되는 외래키 필드 user_id가 생성되지 않음
  - 그래서 기본값을 어떻게 작성할 것인지 선택해야 함
  - 1을 입력하고 Enter 진행 (다음 화면에서 직접 기본 값 입력)

  - article의 user_id에 어떤 데이터를 넣을 것인지 직접 입력해야함
  - 마찬가지로 1 입력하고 Enter 진행
  - 그러면 기존에 작성된 게시글이 있다면 모두 1번 회원이 작성한 것으로 처리

# 2.2. Article & User - CRUD 구현

### Article CREATE

- ArticleForm 출력 필드 수정

``` python
# articles/forms.py

class ArticleForm(forms.ModelForm):

    class Meta:
      model = Article
      fields = ('title', 'content',)
```

- 게시글 작성 시 user_id 필드 데이터가 누락되어 에러 발생

- 게시글 작성 시 작성자 정보가 함께 저장될 수 있도록 save의 commit 옵션 활용

### Article READ

- index 템플릿과 detail 템플릿에서 각 게시글의 작성자 출력 및 확인

``` html
<!-- articles/index.html -->

  <h3>DETAIL</h3>
  <p>후기 번호 - {{review.pk}}</p>
  <p>후기 제목 - {{review.title}}</p>
  <p>후기 내용 - {{review.content}}</p>
  <p>영화 이름 - {{review.movie}}</p>
```

### Article UPDATE
- 수정을 요청하려는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 수정할 수 있도록 함

``` python
@login_required
def update(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    
    # 수정을 요청하는 자 vs 게시글의 작성자 비교
    if request.user == review.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('reviews:detail', review.pk)
        else:
            form = ReviewForm(instance=review)
    else:
        return redirect('reviews:index', review_pk)
```

- 해당 게시글의 작성자가 아니라면, 수정/삭제 버튼을 출력하지 않도록 함

```html
<!-- articles/detail.html -->

{% if request.user == comment.user %}
  <a href="{% 'url articles:update' article.pk %}">UPDATE</a><br>
  <form action="{% url 'reviews:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="DELETE">
  </form>
{% endif %}
```

### Article DELETE
- 삭제를 요청하려는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 삭제할 수 있도록 함

``` python
# articles/views.py

@login_required
def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user: # 게시글 작성자 == 본인
        review.delete()
    return redirect('reviews:index')
```

# 3.1. Comment & User - 모델 관계 설정

### User 외래키 정의

``` python
# articles/models.py


class Comment(models.Model):
    article = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(null=False)
```

- migration 진행

# 3.2. Comment & User - CRD 구현

### Comment CREATE
- 댓글 작성 시 작성 정보가 함께 저장될 수 있도록 save의 commit 옵션 활용

### Comment READ
- detail 템플릿에서 각 댓글의 작성자 출력 및 확인

``` html
<!-- articles/detail.html -->

{% for comment in comments %}
  <li>
    {{ comment.user }} - {{ comment.content }}
  </li>
{% endfor %}
```

### Comment DELETE
- 삭제를 요청한 사람과 댓글을 작성한 사람을 비교하여 본인의 댓글만 삭제할 수 있도록 함
- 해당 댓글의 작성자가 아니라면, 댓글 삭제 버튼을 출력하지 않도록 함