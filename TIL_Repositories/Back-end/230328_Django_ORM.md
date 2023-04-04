# 06. Django - Django Model

## 학습 목표

> django ORM을 사용해 QuerySet이란 무엇인지 이해하고, 데이터베이스에서 데이터를 가져오는 방법을 습득한다.

> QuerySet에서 데이터를 필터링하는 다양한 방법들을 학습하고, 적절한 방법을 선택할 수 있는 API를 학습한다.

# 1. 개요

### ORM(Object-Relational-Mapping)
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 프로그래밍 기술

# 2. QuerySet API

### QuerySet API
- ORM에서 데이터를 검색, 필터링, 정렬 밑 그룹화 하는데 사용하는 도구
-(API를 사용하여 SQL이 아닌 PYTHON 코드로 데이터를 처리)

### QuerySet API 구문

> Article.objects.all()

- Model class, Manager, Queryset API

### Query
- 데이터베이스에 특정한 데이터를 보여달라는 요청
- "쿼리문을 작성한다"
  - 원하는 데이터를 얻기 위해 데이터베이스의 요청을 보낼 코드를 작성한다.
- 이 때, 파이썬으로 작성한 코드가 ORM에 의해 SQL로 변환되어 데이터베이스에 전달되며, 데이터베이스의 응답 데이터를 ORM이 QuerySet이라는 자료 형태로 변환하여 우리에게 전달

### QuerySet
- 데이터베이스에게서 전달 받은 객체 목록(데이터 모음)
  - 순회가 가능한 데이터로써 1개 이상의 데이터를 불러와 사용할 수 있음
- Django ORM을 통해 만들어진 자료형
-단, 데이터베이스가 단일한 객체를 반환 할 때는 QuerySet이 아닌 모델(Class)의 인스턴스로 반환됨

# 3. ORM CREATE
### QuerySet API 실습 사전 준비
- 외부 라이브러리 설치 및 설정

> $ pip install ipython

> $ pip install django-extensions

``` python
INSTALLED_APPS = [
  'articles',
  'django_extensions',
...,
]
```

> pip freeze > requirements.txt

### Django Shell
- django 환경 안에서 실행되는 python shell
- (입력하는 QuerySet API 구문이 django 프로젝트에 영향을 미침)

## 데이터 객체를 만드는(생성하는) 3가지 방법

### 생성 1번째 방법
``` Python
# Article 클래스의 인스턴스 생성
article = Article()

# article 인스턴스에 title과 content 인스턴스 변수에 값을 저장
article.title = '제목'
article.content = '내용'

# 테이블에 레코드 하나 생성을 위해 저장 (인스턴스 메서드 save 호출)
article.save()
```

### 생성 2번째 방법
``` python
article = Article(title='second', content='django!')
article.save()
```

### 생성 3번째 방법
- QuerySet API 중에 create 메서드를 활용

``` Python
Article.objects.create(title='third', content='django!')
```

# 4. ORM READ

### 전체 데이터 조회

> Article.objects.all()

### 단일 데이터 조회

> Article.objects.get(pk=1)

> Article.objects.get(pk=100)

> Article.objects.get(content='django!')

### get()
- 객체를 찾을 수 없으면 DoesNotExist 예외를 발생시키고, 둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외를 발생시킴
- `위와 같은 특징을 가지고 있기 때문에 primary key와 같이 고유성(uniqueness)을 보장하는 조회에서 사용해야 함

### 특정 조건 데이터 조회

### 단일 데이터 조회

> Article.objects.filter(content='django!')

> Article.objects.filter(title='a')

> Article.objects.filter(title='first')

# 99. 참고

### Field lookups
- 특정 레코드에 대한 조건을 설정하는 방법
- QuerySet 메서드 filter(), exclude() 및 get()에 대한 키워드 인자로 지정됨

``` Python
# Field lookups 예시

# "content 컬럼에 'dj'가 포함된 모든 데이터 조회"
Article.objects.filter(content__contains='dj')
```

### ORM, QuerySet API를 사용하는 이유
- 데이터베이스 쿼리를 추상화하여 Django 개발자가 데이터베이스와 직접 상호작용하지 않아도 되도록 함
- 데이터베이스와의 결합도를 낮추고 개발자가 더욱 직관적이고 생산적으로 개발할 수 있도록 도움