# 사용자 정의 함수

> 함수를 직접 정의하고 활용할 수 있다.

> 함수 정의에 맞춰 함수를 호출하고 실행시킬 수 있다.

> 함수의 스코프를 이해하고 설명할 수 있다.

> 파이썬의 이름 검색 규칙을 설명할 수 있다.


## 선언과 호출
- 함수의 선언은 `def` 키워드를 활용함
- 들여쓰기를 통해 Function body(실행될 코드 블록)를 작성함
- 함수는 parameter를 넘겨줄 수 있음
- 함수는 동작 후에 return을 통해 결과값을 전달함
- 함수는 `함수명()`으로 호출

``` python 
def foo(): # 정의

    return True

foo() # 호출
```

## return
- 함수는 반드시 값을 하나만 return함.
    - 명시적인 return이 없는 경우에도 None을 반환
- 함수는 return과 동시에 실행이 종료됨.

## 함수의 입력(Input)
- parameter : 함수를 실행할 때, 함수 내부에서 사용되는 식별자
- Argument : 함수를 호출할 때, 넣어주는 값

## Argument란?
- 함수 호출 시 함수의 parameter를 통해 전달되는 값
- Argument는 소괄호 안에 할당 func_name(argument)
    - 필수 Argument : 반드시 전달되어야 하는 argument
    - 선택 Argument : 값을 전달하지 않아도 되는 경우는 기본 값이 전달


### position arguments
- 기본적으로 함수 호출 시 Argument는 위치에 따라 함수 내에 전달 됨

### keyword arguments
- 직접 변수의 이름으로 특정 Argument를 전달할 수 있음
- Keyword Argument 다음에 Position Argument를 활용할 수 없음

### Default Arguments values
- 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함
    - 정의된 것보다 더 적은 개수의 argument들로 호출될 수 있음

### 정해지지 않은 개수의 keyword arguments
- 여러 개의 Positonal Argument를 하나의 필수 parameter로 받아서 사용
- Argument들은 **`튜플`** 로 묶여 처리되며, **`parameter에 *를 붙여 표현`**
- 함수가 임의의 개수 Arguments를 Keyword Argument로 호출될 수 있도록 지정
- Argument들은 **`딕셔너리`** 로 묶여 처리되며, **`parameter에 **를 붙여 표현`**

## 함수의 범위(Scope)
- 함수는 코드 내부에 local space를 생성하며, 그 외의 공간인 global scope로 구분
- scope
    - global scope : 코드 어디에서든 참조할 수 있는 공간
    - local scope : 함수가 만든 scope, 함수 내부에서만 참조 가능
- variable
    - global variable : global scope에 정의된 변수
    - local variable : local scope에 정의된 변수

### 객체 수명주기
- 객체는 각자의 수명주기(lifecycle)가 존재
- built-in cycle
    - 파이썬이 실행된 이후부터 영원히 유지
- global scope
    - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때 까지 유지
- local scope
    - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

## 이름 검색 규칙(Name Resolution)
- 파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있음
- 아래와 같은 순서로 이름을 찾아나가며, LEGB Rule이라고 부름
- 함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정할 수 없음

### LEGB Rule
- Local scole : 함수
- Enclosed scope : 특정 함수의 상위 함수
- Global scope : 함수 밖의 변수, Import 모듈
- Built-in scope : 파이썬 안에 내장되어 있는 함수 또는 속성


