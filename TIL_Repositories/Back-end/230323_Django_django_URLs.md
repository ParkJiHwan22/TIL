# 04. django - django URLs

## 학습 목표

> Dispatcher로서의 django URL을 정의하고 어떻게 작동하는지 이해할 수 있다.

> URL 패턴 작성 방법을 이해하고, URL의 변수 추출하는 방법을 사용할 수 있다.

> URL에 이름을 붙여 별칭을 사용하여 쉽게 참조할 수 있다.

# 1. 개요

### URL dispatcher
- 운항 관리자, 분배기
- URL 패턴을 정의하고 해당 패턴이 일치하는 요청을 처리할 view 함수를 연결(매핑)

# 2. 변수와 URL
- 템플릿의 많은 부분이 중복되고, URL의 일부만 변경되는 상황이라면, 계속해서 비슷한 URL과 템플릿을 작성해 나가야 할까?

### Variable Routing
- URL 일부에 변수를 포함시키는 것
- 변수는 view 함수의 인자로 전달할 수 있음

### Variable routing 작성법

``` Python
path('articles/<int:num>/', views.hello)
path('hello/<str:name>/, views.greeting)
```

### Path converters
- URL 변수의 타입을 지정
- (str, int 등 5가지 타입 지원)

### 3. APP의 URL

### APP URL mapping
- 각 앱에 URL을 정의하는 것
- 프로젝트와 각각의 앱이 URL을 나누어 관리하며 주소 관리를 편하게 하기 위함

