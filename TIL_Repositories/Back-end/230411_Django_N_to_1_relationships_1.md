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

# 2. Comment & Article

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

