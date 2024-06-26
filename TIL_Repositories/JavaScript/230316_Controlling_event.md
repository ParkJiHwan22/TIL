# 07. JS - Controlling event

## 학습 목표

> 이벤트 객체의 속성과 관련 메서드를 이해하고 사용할 수 있다.

> addEventListener를 사용해 각 DOM 요소에서 일어나는 이벤트를 감지하고 처리할 수 있다.

# 1. 개요

### 일상 속의 이벤트
- 버튼을 눌러서 도어락을 열거나, 전화기의 버튼을 눌러서 통화를 시작하는 것
- 키보드를 사용하여 글을 쓰거나, 리모컨을 사용하여 채널을 변경하는 것
- 알람 시계를 설정하여 특정 시간에 알림을 받는 것

### 웹에서의 이벤트
- 버튼을 클릭했을 때 모달이 출력되는 것
- 마우스 커서의 위치에 따라 드래그 앤 드롭하는 것
- 사용자가 입력한 값에 따라 새로운 요소를 생성하는 것
- **`일상생활의 이벤트처럼 웹에서도 이벤트를 통해 특정 동작을 수행한다.`**

# 2. 이벤트

## event
- 무언가 일어났다는 신호, 사건(모든 DOM 요소는 이러한 신호를 만들어 냄)

### event 종류
- 마우스, 인풋, 키보드, 터치 등

### DOM 요소는 event를 받고, 받은 event를 '처리'할 수 있음

### event handler
- 이벤트가 발생했을 때 실행되는 함수(사용자의 행동에 어떻게 반응할지를 JS 코드로 표현한 것)

### .addEventListener()
- 대표적인 이벤트 핸들러 중 하나(특정 이벤트를 DOM 요소가 수신할 때마다 콜백 함수를 호출)

``` JavaScript
EventTarget.addEventListener(type, handler)
// DOM 요소            특정 이벤트 콜백 함수
```

- `대상(DOM 요소)`에 `특정 이벤트`가 발생하면 `할 일(콜백 함수)`을 등록함

### EventTarget.addEventListener(type, handler)
- type: 이벤트 이름(ex. 'click')
- handler: 발생한 이벤트 객체를 수신하는 콜백 함수, 콜백 함수는 발생한 Eventobject를 유일한 매개변수로 받음

# 3. 이벤트 핸들러 활용

### click 이벤트

### input 이벤트
- 사용자의 입력 값을 실시간으로 출력하기

### click & input 이벤트
- 사용자의 입력 값을 실시간으로 출력하기
- 버튼을 클릭하면 출력한 값의 스타일을 변경하기

### 이벤트 취소하기
- 텍스트를 복사하려고 하면 알림 창을 띄우면서 복사를 중단하기

### 이벤트 취소하기

### .preventDefault()
- 현재 Event의 기본 동작을 중단

### todo 실습
- 할 일을 입력하고 버튼을 클릭하면 할 일 요소를 생성
- input 컨텐츠를 작성하지 않는다면 경고 알림 출력

### lodash
- 모듈성, 성능 및 추가 기능을 제공하는 JavaScript 유틸리티 라이브러리
- array, object등 자료구조를 다룰 때 사용하는 유용하고 간편한 함수들을 제공

# 99. 참고

### addEventListener와 this
- addEventListener에서의 콜백 함수는 특별하게 function 키워드의 경우 addEventListener를 호출한 대상(event.target)을 뜻함