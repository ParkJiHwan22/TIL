# JavaScript

### 자바스크립트
- 프로토타입 기반 객체 생성을 지원하는 동적 스크립트 언어
- 웹 브라우저에서 주로 사용, Node.js를 이용하여 콘솔 환경에서 사용
- 웹 브라우저의 UI를 제어하기 위해 만들어진 프로그래밍 언어
- 자바와 기본 구문이 비슷(C언어의 기본 구문을 바탕)
- 브랜든 아이크 개발(1995)
- Mocha -> LiveScript -> JavaScript

# 기본 문법

### HTML 자바스크립트 사용
- <script></script> 태그를 사용
- 문서 내의 위치의 제약이 없다.

``` html
<html>
<head>
  <meta charset="UTF-8">
  <title>JavaScript</title>
  <script>console.log('head');</script>
</head>
<body>
  <script>console.log('body');</script>
</body>
</html>
```

### 외부스크립트 참조하기
- .js 확장자를 가진 파일을 생성
- html 문서에서 <script src="외부파일의 위치"></script>

### 주석(Comment)
- // 한 줄 주석
- /* */ 여러 줄 주석

### 변수(Variable)
- 자바스크립트의 변수 타입은 가리키는 값에 대한 타입을 나타냄
- var, let, const 키워드를 이용해서 변수를 선언
- var를 이용한 변수의 선언일 경우 중복 선언이 가능
- undefinded는 변수에 아무 값도 없어서 타입을 알 수 없는 경우를 말함
- 동적 타입: 대입되는 값에 따라서 용도가 변경되는 방식
- 문자, $, _로 시작, 대소문자 구분, 예약어 사용 x

### var
- 재 선언이 가능, 재 할당 가능
- ES6 이전에 변수 선언 시 사용
- 호이스팅(Hoisting) 특성이 있음
- 함수 스코프

``` javaScript
var id = "kim";
console.log(id);
var id = "son";
console.log(id);
```

### let
- 재 선언 불가, 재 할당 가능
- 블록 스코프

``` javaScript
let id = "kim";
console.log(id);
let id = "son";
console.log(id);
```
