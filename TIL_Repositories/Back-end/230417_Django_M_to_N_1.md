# 18. Django - M_to_N_relationships_1

## 학습 목표

> Many to Many Field를 사용하여 다대다 관계를 설정할 수 있다.

> 다대다 관계의 생성, 수정, 삭제 등의 작업을 어떻게 수행하는지를 이해하고 활용할 수 있다.

> 다대다 관계에서 중계 모델(intermediate model)이 필요한 이유와 중개 모델을 어떻게 정의하고 활용하는지에 대해 열거할 수 있다.

# 1. 개요

### M:N 관계 맛보기
- 병원 진료 시스템 모델 관계 만들기(환자 - 의사)

### N:1의 한계
- 한 명의 의사에게 여러 환자가 예약할 수 있다고 모델 관계를 설정

``` python
# hospitals/models.py

class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
```

- 각각 2명의 의사와 환자를 생성하고 환자는 서로 다른 의사에게 예약했다고 가정

- 1번 환자가 두 의사 모두 방문하려고 할 때 문제 발생

- 의사 객체를 하나 더 만들어서 예약을 진행하거나 새로운 환자 객체를 생성해야 함

- 해결 방법 : `예약 테이블을 따로 만들자`

### 중개 모델

- 환자 모델의 외래 키를 삭제하고 별도의 예약 모델을 새로 작성

- 예약 모델은 의사와 환자에게 각각 N:1 관계를 가짐

``` python
# hospitals/models.py

# 외래 키 삭제
class Patient(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

# 중개모델 작성
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.doctor.id}번 의사의 {self.patient_id}번 환자'
```

- 데이터베이스 초기화 후 Migration 진행 및 shell_plus 실행

- 의사와 환자 생성 후 예약 만들기

``` python
doctor1 = Doctor.objects.create(name='alice')
patient1 = Doctor.objects.create(name='carol')

Reservation.objects.create(doctor=doctor1, patient=patient1)
```

- 예약 정보 조회

``` python
# 의사 -> 예약 정보 찾기
doctor1.reservation_set.all()

patient1.reservation_set.all()
```

- 1번 의사에게 새로운 환자 예약이 생성된다면

``` python
patient2 = Patient.objects.create(name='dane')

Reservation.objects.create(doctor=doctor1, patient=patient2)
```

- 1번 의사의 예약 정보 조회

``` python
# 의사 -> 환자 목록
doctor1.reservation_set.all() # 1번 의사의 1번 환자, 2번 환자
```

### Django ManyToManyField

- 환자 모델에 Django ManyToManyField 작성

``` python
from django.db import models
# hospitals/models.py

class Patient(models.Model):
    # ManyToManyField 작성
    doctors = models.ManyToManyField(Doctor)
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
```

- 생성된 중개 테이블 hospitals_patient_doctors 확인

- 의사 1명과 환자 2명 생성

``` python
doctor1 = Doctor.objects.create(name='alice')
patient1 = Patient.objects.create(name='carol')
patient2 = Patient.objects.create(name='dane')
```

- 예약 생성(환자가 의사에게 예약)

``` python
# patient1이 doctor1에게 예약
patient1.doctors.add(doctor1)

# patient1 - 자신이 예약한 의사목록 확인
patient1.doctors.all()

# doctor1 - 자신이 예약된 환자목록 확인
doctor1.patient_set.all()
```

- 예약 생성(의사가 환자를 예약)

``` python
# doctor1이 patient2을 예약
doctor1.patient_set.add(patient2)

# doctor1 - 자신이 예약한 환자목록 확인
doctor1.patient_set.all()

# patient1, 2 - 자신이 예약한 의사목록 확인
patient2.doctors.all()

patient1.doctors.all()
```

- 예약 취소하기(삭제)

- 기존의 경우, 해당하는 Reservation을 찾아서 지워야 했다면, 이제는 remove()사용

``` python 
# doctor1이 patient1 진료 예약 취소

doctor1.patient_set.remove(patient1)
doctor1.patient_set.all()
patient1.doctors.all()

# patient2가 doctor1 진료 예약 취소

patient2.patient_set.remove(doctor1)
patient2.doctors.all()
doctor1.patient_set.all()
```

### 'through' argument
- 중개 모델을 직접 작성하는 경우
- 중개 테이블을 수동으로 지정하려는 경우 through 옵션을 사용하여 사용하려는 중개 테이블을 나타내는 Django 모델을 지정할 수 있음
- 가장 일반적인 용도: `중개 테이블에 '추가 데이터'를 사용해 다대다 관계와 연결하려는 경우`

- through 설정 및 Reservation Class 수정
- 이제는 예약 정보에 "증상"과 "예약일"이라는 추가 데이터가 생김

``` python
class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor, through='Reservation')
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'


class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'
```

- 데이터베이스 초기화 후 Migration 진행 및 shell_plus 실행
- 의사 1명과 환자 2명 생성

``` python
doctor1 = Doctor.objects.create(name='alice')
patient1 = Patient.objects.create(name='carol')
patient2 = Patient.objects.create(name='dane')
```

- 예약 생성 방법 1

``` python
# 1. Reservation class를 통한 예약 생성

reservation1 = Reservation(doctor=doctor1, patient=patient1, symptom='headache')
reservation1.save()
doctor1.patient_set.all()
patient1.doctors.all()
```

- 예약 생성 방법 2

``` python
# 2. Patient 객체를 통한 예약 생성
patient2.doctors.add(doctor1, through_defaults={'symptom': 'flu'})
doctor1.patient_set.all()
patient2.doctors.all()
```

- 예약 삭제

``` python
doctor1.patient_set.remove(patient1)

patient2.doctors.remove(doctor1)
```

### 정리

- M:N 관계로 맺어진 두 테이블에는 변화가 없음
- ManyToManyField는 중개 테이블을 자동으로 생성함
- ManyToManyField는 M:N 관계를 맺는 두 모델 어디에 위치해도 상관 없음
- 대신 필드 작성 위치에 따라 참조와 역참조 방향을 주의할 것
- N:1은 완전한 종속의 관계였지만 M:N은 의사에게 진찰받는 환자, 환자를 진찰하는 의사의 두 가지 형태로 모두 표현이 가능

# 2. ManyToManyField

### ManyToManyField(to, **options)
- many-to-many 관계 설정 시 사용하는 모델 필드
- 모델 필드의 RelatedManager를 사용하여 관련 개체를 추가, 제거 또는 생성
  - add(), remove(), create(), clear()

### 1. related_name
- 역참조시 사용하는 manager name을 변경

``` python
class Patient(models.Model):
    doctor = models.ManyToManyField(Doctor, related_name='patients')
    name = models.TextField()
```

``` python
# 변경 전
doctor.patient_set.all()

# 변경 후
doctor.patients.all()
```

### 2. through
- 중개 테이블을 직접 작성하는 경우, through 옵션을 사용하여 중개 테이블으 나타내는 Django 모델을 지정

- 일반적으로 중개 테이블에 추가 데이터를 사용하는 다대다 관계와 연결하려는 경우
(extra data with many-to-many relationship)에 사용됨

### 3. symmetrical
- ManyToManyField가 동일한 모델을 가리키는 정의에서만 사용

``` python
# 예시

class Person(models.Model):
    friends = models.ManyToManyField가('self')
    # friends = models.ManyToManyField가('self', symmetrical=False)
```

- True일 경우
    - _set 매니저를 추가하지 않음
    - source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면 자동으로 target 모델 인스턴스도 source 모델 인스턴스를 자동으로 참조하도록 함(대칭)
    - 내가 당신의 친구라면 당신도 내 친구가 됨

- 대칭을 원하지 않는 경우 False로 설정
    - Follow 기능 구현에서 다시 확인

### M:N에서의 methods
- add()
    - `지정된 객체를 관련 객체 집합에 추가`
    - 이미 존재하는 관계에 사용하면 관계가 복제되지 않음

- remove()
    - `관련 객체 집합에서 지정된 모델 개체를 제거`

# 3. Article & User

### Many to many relationships(N:M or M:N)
- 한 테이블의 0개 이상의 레코드가 다른 테이블 0개 이상의 레코드와 관련된 경우

- `양쪽 모두에서 N:1 관계를 가짐`

### Article(M) - User(N)
- 0개 이상의 게시글은 0명 이상의 회원과 관련됨
- 게시글은 회원으로부터 0개 이상의 좋아요를 받을 수 있고, 회원은 0개 이상의 게시글에 좋아요를 누를 수 있다.

### 모델 관계 설정
- ManyToManyField 작성

``` python
# articles/models.py

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=80)
    content = models.TextField(null=False)
```

- Migration 진행 후 에러 확인

- like_users 필드 생성 시 자동으로 역참조에는 .article_set 매니저가 생성됨

- 그러나 이전 N:1(Article-User)관계에서 이미 해당 매니저를 사용 중
    - user.article_set.all() -> 해당 유저가 작성한 모든 게시글 조회

- user가 작성한 글들(user.article_set)과 user가 좋아요를 누른 글(user.article_set)을 구분할 수 없게 됨

- user와 관계된 ForeignKey 혹은 ManyToManyField 중 하나에 related_name을 작성해야 함

- N:1과 M:N에서 `related manager 이름이 충돌`

- related_name 작성 후 Migration

``` python
# articles/models.py

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    title = models.CharField(max_length=80)
    content = models.TextField(null=False)
```

### User - Article간 사용 가능한 related manager 정리

- article.user: 게시글을 작성한 유저 -> N:1

- user.article_set: 유저가 작성한 게시글(역참조) -> N:1

- article.like_users: 게시글을 좋아요 한 유저 -> M:N

- user.like_articles: 유저가 좋아요한 게시글(역참조) -> M:N

### 좋아요 구현
- url 및 view 함수 작성

``` python
# articles/urls.py

urlpatterns = [
    ...
    path('<int:article_pk>/likes/', views.likes, name='likes'),
]
```

``` python
# articles/views.py

@login_required
def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    
    if request.user in article.like_users.all():
        # 좋아요 취소
        article.like_users.remove(request.user)
    else:
        # 좋아요 추가
        article.like_users.add(request.user)
    return redirect('articles:index')
```

``` html
<!-- articles/index.html -->

<form action="{% url 'articles:likes' article.pk %}" method="POST">
    {% csrf_token %}
    {% if request.user in article.like_users.all %}
    <input type="submit" class="emoji" value="좋아요 취소">
    {% else %}
    <input type="submit" class="emoji" value="좋아요">
    {% endif %}
</form>
```

# 99. 참고

### .exists()
- QuerySet에 결과가 포함되어 있으면 True를 반환하고 그렇지 않으면 False를 반환
- 특히 큰 QuerySet에 있는 특정 개체의 존재와 관련되 검색에 유용

``` python
# articles/views.py

@login_required
def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)
    return redirect('articles:index')
```