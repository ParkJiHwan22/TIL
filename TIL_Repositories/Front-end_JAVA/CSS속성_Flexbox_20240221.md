# CSS 속성

### 어제 복습

- form은 정보 전달을 위한 주머니
- label은 input태그를 위한 것

### 크기 단위
- 내용 길이 값(length): px, cm, mm, in, `em`, `rem` 등의 길이 단위 사용
- 백분율(%): 상위 block에 대한 백분율의 단위, 상위 block 크기가 바뀌면 자신의 크기도 자동으로 변경
- auto (width): 100%, 자신의 상위 block이 허용하는 width 크기만큼 채운다.
- auto (height): 0%, 높이를 결정하는 요인은 block box 속의 내용물의 크기

- `left width, right width auto로 하면 가운데에 정렬`

### 색상 단위
- 색상 키워드: 대소문자 구분 ex. red, blue ...
- RGB 색상: 16진수 표기법 혹은 함수형 표기법을 사용해서 특정 색을 표현하는 방식
- HSL 색상: 색상, 채도, 명도를 통해 특정 색을 표현하는 방식

### font

|속성|의미|
|--|--|
|font-family|글꼴 지정(font name)|
|font-size|글자 크기 지정|
|font-style|글자 스타일 지정, oblique-> 비스듬히|
|font-variant|소문자를 작은 대문자(small-caps)로 변형|
|font-weight|글자 굵기 지정|
|font|font에 관한 속성을 한번에 지정하는 단축형(short hand) 속성, 비추! 쓰지말자|

### text

|속성|의미|
|--|--|
|text-align text|정렬 방식 지정|
|text-decoration|text 장식 지정|
|text-indent|text-block안 첫 라인의 들여쓰기 지정|
|text-transform|text 대문자화|
|white-space|요소(element) 안의 공백 지정|
|vertical-align|수직 정렬 지정|
|letter-spacing|문자 간의 space 간격을 줄이거나 늘림|
|word-spacing|단어 간의 간격 지정|
|line-height|줄(행) 간격 지정|
|color|text 색상 지정|

### background

|속성|의미|
|--|--|
|backgorund-color|배경색을 지정|
|backgorund-image|배경을 이미지로 지정|
|backgorund-attachment|배경 이미지를 고정하거나 scroll여부를 지정|
|backgorund-repeat|배경 그림의 반복 여부를 지정|
|backgorund-position|배경 그림의 위치를 지정|
|backgorund|배경 관련 속성을 한번에 지정(font 속성과 달리 속성 값 순서에 구애받지 않음)|
|backgorund-size|배경 이미지 크기 조절|
|backgorund-clip|배경 적용 범위 조절|

### box model
- 모든 HTML 요소는 box 형태로 되어 있음
- 네모의 세상

- margin: 테두리 바깥 외부 여백
- border: 테두리
- padding: 테두리 안쪽 내부 여백
- box-sizing: 실제 내용

### margin
- marginm 속성은 box의 마진 영역의 너비를 지정

- 값 1개: 모든 면 적용
- 값 2개: { top, bottom } , { right, left }
- 값 3개: { top } , { right, left }, { top }
- 값 4개: top, bottom, right, left 순으로 적용

- margin: 0 auto 를 통해 가운데 정렬이 되도록 설정 가능
- 마진 상쇄 현상이 일어날 수 있음

### border
- border-style: 선의 모양
- border-width: 선의 굵기
- border-color: 선의 색상
- 위 세 속성을 줄여서 사용가능

- border-radius: 선의 모서리를 둥글게 만드는 속성
- box-shadow: 그림자 효과

### padding
- padding 속성은 box의 패딩 영역의 너비를 설정
- 값 1개: 모든 면 적용
- 값 2개: { top, bottom } , { right, left }
- 값 3개: { top } , { right, left }, { top }
- 값 4개: top, bottom, right, left 순으로 적용

### box-sizing
- 기본적으로 모든 요소의 box-sizing은 content-box
- padding을 제외한 순수 contents 영역만을 box로 지정
- border까지의 너비를 크기로 보기 원할 때
- box-sizing: border-box

### display: block
- 줄 바꿈이 일어나는 요소
- 화면 크기 전체의 가로 폭을 차지
- 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음
- 대표적인 블록 레벨 요소
- div
- ul, ol, li
- p
- hr
- form

### display: inline
- 줄 바꿈이 일어나지 않는 행의 일부 요소
- content 너비만큼 가로 폭을 차지
- width, height, margin-top, margin-bottom을 지정할 수 없음
- 상하 여백은 line-height로 지정
- 대표적인 인라인 레벨 요소
- span
- a
- img
- input, label
- b, em, i, strong

### display: inline-block
- block과 inline 레벨 요소의 특징을 모두 갖고 있음
- inline처럼 한 줄에 표시 가능
- block처럼 width, height, margin 속성 지정 가능

### display: none
- 해당 요소를 화면에 표시하지 않음(공간x, 화면x)
- visibility: hidden은 해당 요소(공간o, 화면x)

### position
- static: (기본) 일반적인 내용물의 흐름, 상단, 좌측에서의 거리를 지정할 수 없음
- relative: HTML 문서에서의 일반적인 내용물의 흐름을 말하지만, top, left 거리를 지정
- absolute: 자신의 상위 box속에서의 top, left, right, bottom 등의 절대적인 위치를 지정
- fixedL 스크롤(scroll)이 일어나도 항상 화면상의 지정된 위치에 있음

### float
- float 속성은 박스를 어느 위치에 배치할 것인지를 결정하기 위해 사용
- none: 기본값
- left: 요소를 왼쪽으로 띄움
- right: 요소를 오른쪽으로 띄움

### clear
- float 속성이 가지고 있는 값을 초기화하기 위해 사용
- left, right: 각각의 속성 값을 취소할 수 있음
- both: 양쪽의 float 속성 값을 취소할 수 있음
- none: 기본 값

# Flexbox

### Flexbox
- Flexible Box module은 인터페이스 내의 아이템 간 공간 배분과 강력한 정렬 기능을 제공하기 위한 1차원 레이아웃 모델로 설계

### 주요 개념
- Main Axis(주축), Cross Axis(교차축)
- 시작선(start), 끝선(end)
- Container와 item

### Flex Container
- display 속성을 이용하여 container를 생성
- display: flex; -> block 성격의 container
- display: inline-flex; -> inline 성격의 container

- flex-direction: container 안의 item들의 나열되는 방향
- flex-wrap: container 안의 item들의 크기가 container의 크기보다 클 때 줄 넘김
- flex-flow: 방향과 줄 넘김을 동시에 설정
- justify-content: 메인 축(main axis)의 정렬을 제어
- align-items: 교차 축(cross axis)의 정렬을 제어
- align-content: wrap 속성에 의해서 여러 줄이 발생한 경우 교차 축(cross axis) 정렬

# Appendix

### Flex item
- order: item의 배치 순서 제어
- flex-basis: item의 너비를 지정
- flex-grow: item의 팽창 제어
- flex-shrinkL item의 수축 제어
- flex: flex-grow, flex-shrink, flex-basis의 속성을 단축 지정
- align-self: 특정 item의 교차축(cross axis)정렬을 제거

