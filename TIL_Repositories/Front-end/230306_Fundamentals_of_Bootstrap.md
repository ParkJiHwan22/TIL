# 07. Fundamentals_of_Bootstrap

## 학습 목표

> Bootstrap을 설치하고 기본 구성 요소, UI 요소 및 컴포넌트 사용 방법에 대해 숙지할 수 있다.

> Bootstrap을 이용하여 웹 프로젝트를 구현하는 방법을 익히고, 실습에 적용할 수 있다.

# 1. 개요
## Bootstrap
- 프론트엔드 라이브러리(Toolkit)
- `반응형 웹 디자인 & CSS 및 JS 기반의 컴포넌트와 스타일 제공

## Bootstrap 클래스명 맛보기

``` HTML
<p class="mt-5">Hello, world!</p>
```

- m: {property}
- t: {sides}
- 5: {size}

- 이미 스타일이 작성되어 있고 독특한 규칙이 있는 클래스 이름까지.
- 우리는 설명서를 보며 Bootstrap이라는 도구상자를 어떻게 사용할 지 학습할 것

# 2. Typograpy 및 Color

### Typograpy
- 문서 상에 제목, 본문 텍스트, 목록 등

### Headings
- HTML h1 ~ h6 태그와 스타일을 일치시키고 싶지만 관련 HTML태그를 더 사용할 수 없는 경우

### Display headings
- 기존 Heading보다 더 눈에 띄는 제목이 필요한 경우(더 크고 약간 다른 스타일)

### Inline text elements
- HTML inline 요소에 대한 스타일

### List
- HTML list 요소에 대한 스타일

## Bootstrap Color system
- Bootstrap이 지정하고 제공하는 시스템

### Colors
- Text, Border, Background 및 다양한 요소에 사용하는 Bootstrap의 색상 키워드

# 3. Component

## Bootstrap Component
- Bootstrap에서 제공하는 `UI 관련 요소`
  - `버튼, 폼, 카드, 드롭다운, 네비게이션 바 등`
  - 'for 일관된 디자인, 쉬운 프로토타입 제작 및 사용자 경험

## 대표 Component 사용해보기
- Alerts, Badges, Buttons, Cards, Navbar

# 99. 참고

## CDN(Content Delivery Network)
- 지리적 제약 없이 빠르고 안전하게 콘텐츠를 전송할 수 있는 전송 기술
  - `서버와 사용자 사이의 물리적인 거리를 줄여 콘턴츠 로딩에 소요되는 시간을 최소화(웹 페이지 로드 속도를 높임)`
- 사용자가 해당 서버에서 멀리 떨어져 있는 경우 해당 콘텐츠를 로드하는 데 시간이 오래 걸림
- 지리적으로 사용자와 가까운 CDN 서버에 콘텐츠를 저장해서 사용자에게 전달