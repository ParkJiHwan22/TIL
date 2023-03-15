# 04. JS - Functions

## 학습 목표

> 함수를 정의하는 방법과 함수를 호출하는 방법을 이해할 수 있다.

> 함수를 선언식으로 정의하는 방법과 변수에 할당하는 표현식으로 정의하는 방법을 이해하고 활용할 수 있다.

> 화살표 함수의 개념과 사용법을 이해하고 작성할 수 있다.

> 함수를 사용해 코드를 모듈화하고 재사용성을 높일 수 있다.

# 1. 개요

### 참조 자료형 (objects)
- Object, Array, Function

### Function
- 참조 자료형에 속하며 모든 함수는 Function object

### 함수의 구조
- 함수의 이름
- 함수의 매개변수
- 함수의 body를 구성하는 statement

``` JavaScript
function name ([param[, param[..., param]]]) {
  statements
  return value
}
```
- return 이 없다면 undefined를 반환

# 2. 함수의 정의

## 선언식(function declaration)

``` JavaScript
function name () {
  statements
}
```
## 표현식(function expression)
``` JavaScript
const funcName = function () {
  statements
}
```
### 함수 표현식 특징
- 함수 이름이 없는 '익명 함수'를 사용할 수 있음
- 선언식과 달리 표현식으로 정의한 함수는 호이스팅 되지 않으므로 코드에서 나타나기 전에 먼저 사용할 수 없음

### 선언식과 표현식

| |선언식|표현식|
|--|--|--|
|특징|익명 함수 사용 불가능, 호이스팅 있음|익명 함수 사용 가능, 호이스팅 없음|
|비고||사용권장|

### 기본 함수 매개변수(Default function parameter)
- 값이 없거나 undefined가 전달될 경우 이름 붙은 매개변수를 기본값으로 초기화

### 나머지 매개변수(Rest parameters)
- 무한한 수의 인자를 '배열'로 허용하여 가변 함수를 나타내는 방법

### 화살표 함수 표현식(Arrow function expressions)
- 함수 표현식의 간결한 표현법

### 화살표 함수 표현식 작성 순서
1. function 키워드 제거 후 매개변수와 중괄호 사이에 화살표(=>)작성
2. 함수의 매개변수가 하나 뿐이라면 매개변수의 '()'제거 가능
3. 함수 본문의 표현식이 한 줄이라면 '{}'와 'return'제거 가능