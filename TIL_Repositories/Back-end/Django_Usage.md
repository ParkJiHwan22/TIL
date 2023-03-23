# 1. 개발 환경 설정 가이드 작성
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


# 2. 파일을 받는 팀원 입장

## 1. 가상환경 생성(가상환경 이름 : venv)

> $ python -m venv venv

### 1.1 가상환경 설정 확인

> $ pip list

### 2. 파일 공유받기

> $ pip install -r reqirements.txt


# 3. django 디자인 패턴

### 1. 앱 생성

> $ python manage.py startapp articles

### 2. 앱 등록

``` python
INSTALLED APPS = [
  'articles', # 앱 이름 추가
  'django.contrib.admin',
  'django.contrib.auth',
  ...
]
```

### 3. URLs 설정

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

### 4. View

``` python
def index(request):
  return render(request, 'articles/index.html')
```

- 특정 경로에 있는 template과 request 객체를 결합해 응답 객체를 반환하는 index view 함수 정의

### 5. Template
- articles 앱 폴더 안에 templates 폴더 작성
- templates 폴더 안에 템플릿 페이지 작성


