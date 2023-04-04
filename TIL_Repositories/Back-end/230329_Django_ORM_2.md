# 07. Django - ORM

## 학습 목표

> QuerySet API를 사용해 데이터를 수정하고 삭제하는 방법을 익힌다.

# 1. ORM UPDATE

### 데이터 수정

``` python
# 수정할 인스턴스 조회
>>> article = Article.objects.get(pk=1)

# 인스턴스 변수를 변경
>>> article.title = 'byebye'

# 저장
>>> article.save()

# 정상적으로 변경된 것을 확인
>>> article.title
'byebye'
```

# 2. ORM DELETE

### 데이터 수정

``` python
# 삭제할 인스턴스 조회
>>> article = Article.objects.get(pk=1)

# delete 메서드 호출 (삭제 된 객체가 반환)
>>> article.delete()
(1, {' articles.Article ' : 1})

# 삭제한 데이터는 더이상 조회할 수 없음
>>> Article.objects.get(pk=1)
DoesNotExist: Article matching query does not exist.
```