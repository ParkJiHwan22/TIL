# Python 기초

## <목차>
컴퓨터 프로그래밍 언어

## <학습 목표>

> 컴퓨커 프로그래밍 언어를 정의할 수 있다.

> VS Code를 활용하여 파이썬 코드를 작성하고 실행할 수 있다.

> 변수를 정의하고 활용할 수 있다.

> 파이썬 주요 객체(타입)의 특징을 비교하고 설명할 수 있다.

> 객체에 맞춰 연산자를 활용할 수 있다.

## 컴퓨터 프로그래밍 언어

- 컴퓨터(computer) : Caculation(조작) + Remember(저장)
- 프로그래밍(`Program`ming) : `명령어의 모음(집합)`
- 언어 : `자신의 생각을 나타내고 전달하기` 위해 사용하는 체계, `문법적`으로 맞는 말의 집합
- 컴퓨터 프로그래밍 언어 : 컴퓨터에게 명령하기 위한 약속

- 선언적 지식(declarative knowledge) : 사실에 대한 내용
- `명령적 지식(imperative knowledge) : How-to`

## 파이썬(Python)
- Easy to Learn
    - 다른 프로그래밍 언어보다 문법이 간단하면서도 엄격하지 않음
    - 문법 표현이 매우 간결하여 프로그래밍 경험 없어도 짧은 시간 내에 마스터할 수 있음
- Expressive Language
- 크로스 플랫폼 언어
- 인터프리터 언어
    - 소스코드를 기계어로 변환하는 컴파일 과정 없이 바로 실행 가능
    - 코드를 대화하듯 한 줄 입력하고 실행한 후, 바로 확인할 수 있음
- 객체 지향 프로그래밍

## 객체와 변수
- 객체 : 프로그래밍 언어에서 저장을 하고 조작을 할 때, 그 곳에 담기는 모든 것
- 변수 : 컴퓨터 메모리가 어딘가에 저장되어 있는 객체를 참조하기 위해 사용되는 이름
- 변수는 박스안에 담겨있는 객체이다.

변수 : 할당 연산자(=)를 통해 값을 할당(assignment)
- **`type()`**
    - 변수에 할당된 값의 타입
    ``` python
    name = '박지환'
    print(type(name)) # <class 'str'>
    ```
- 변수 할당

    - 같은 값을 동시에 할당할 수 있음

    ``` python
    x = y = 1004
    ```

    - 다른 값을 동시에 할당 할 수 있음(multiple assignment)

    ``` python
    x, y = 1, 2
    ```

- 실습 문제
    - X = 10, Y = 20 일 때, 각각 바꿔서 저장하는 코드를 작성하시오.

    ``` python
    tmp = x # 방법 1) 임시 변수 활용
    x = y
    y = tmp
    print(x, y)
    ```

    ``` python
    x, y = y, x # 방법 2) Pythonic
    print(x, y)
    ```

식별자(Identifiers)
- 파이썬 객체(변수, 함수, 모듈, 클래스 등)를 식별하는데 사용하는 이름(name)
- 규칙
    - 식별자의 이름은 영문 알파벳, `언더스코어(_)`, 숫자로 구성
    - 첫 글자에 숫자가 올 수 없음
    - 길이 제한이 없고, 대소문자를 구별
    - 다음의 키워드는 예약어로 사용할 수 없음

    ```
    False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lamda, nolocal, not, or, pass, raise, return, try, while, with, yield
    ```

    - 내장함수나 모듈 등의 이름으로도 만들면 안됨

- 파이썬은 동적 타이핑이기 때문에 어떤 타입인지 알아두는 것이 중요함

## 자료형 (Data Type)
- 객체(object)의 종류 : Type

### 자료형 분류

1. 숫자
    - 수치형(numeric Type)
        - int(정수, interger)
        - float(부동소수점, 실수, floating point number)
        - complex(복소수, complex number)
    - 불린형(Boolean Type)

2. 시퀀스(Sequence)
    - 문자열(String)
    - 튜플(Tuple)
    - 리스트(List)
    - 레인지(Range)

3. 컬렉션(Collection)
    - 집합(Set)
    - 딕셔너리(Dictionary)

4. None

## **`수치형(Numeric Type)`**

### `정수(Int)`
- 모든 정수의 타입은 `int`
- 매우 큰 수라 하더라도 오버플로우가 발생하지 않음

### 실수(Float)
- 정수가 아닌 모든 실수는 float 타입
- 부동소수점
    - 실수가 컴퓨토를 표현하는 방법 - 2진수(비트)로 숫자를 표현
- 부동소수점에서 실수 연산 과정에서 발생 가능
    - 값을 비교하는 과정에서 `정수가 아닌 실수`인 경우 주의 할 것
    - 매우 작은 수보다 작은지를 확인하거나 math 모듈 활용

### 복소수(Complex)
- 실수부와 허수부로 구성된 복소수는 모두 complex 타입

### `불린형(Boolean Type)`
- `True(1)` / `False(0)` 값을 가진 타입은 bool
- 비교/논리 연산을 수행함에 있어서 활용됨
- 다음은 모두 False로 변환

```
0, 0.0, (), [], ", None 
```

## 연산자(Operator)

### 산술연산자(Arithmetic Operator)
- 기본적인 사칙연산 및 수식 계산

    - |연산자|내용|
      |--|--|
      |+|덧셈|
      |-|뺄셈|
      |*|곱셈|
      |`%`|`나머지`|
      |/|나눗셈|
      |`//`|`몫`|
      |`**`|`거듭제곱`|
    
### 복합 연산자(In-place Operator)
- 연산과 할당이 함께 이루어짐

    - |연산자|내용|
      |--|--|
      |a += b|a = a + b|
      |a -= b|a = a - b|
      |a *= b|a = a * b|
      |a /= b|a = a / b|
      |a //= b|a = a // b|
      |a %= b|a = a % b|
      |a ** b|a = a ** b|

### 비교 연산자(Comparison Operator)
- 값을 비교하며, True/ False 값을 리턴함
    - |연산자|내용|
      |--|--|
      |<|미만|
      |<=|이하|
      |>|초과|
      |>=|이상|
      |`==`|`같음`|
      |`!=`|`같지 않음`|

### 논리 연산자(Logical Operator)
- 논리식을 판단하여 참(True)와 거짓(False)를 반환함
    - |연산자|내용|
      |--|--|
      |A and B|A와 B 모두 True시, True|
      |A or B|A와 B 모두 False시, False|
      |Not|True를 False로, False를 True로|
    - and : 모두 참인 경우 참, 그렇지 않으면 거짓
    - or : 둘 중 하나만 참이라도 참, 둘 다 거짓일 경우 거짓
    - not : 참 거짓의 반대 결과

## 컨테이너(Container)
- 여러 개의 값을 담을 수 있는 것(객체)
- 순서가 있는 데이터(Ordered) vs 순서가 없는 데이터(Unordered)로 구분함

- 컨테이너 분류
    - 시퀀스
        - 문자열(immutable) : 문자들의 나열
        - 리스트(mutable) : `변경 가능`한 값들의 나열
        - 튜플(immutable) : `변경 불가능`한 값들의 나열
        - 레인지(immutable) : 숫자의 나열
    - 컬렉션/비시퀀스
        - 세트(mutable) : `유일한 값`들의 모음
        - 딕셔너리(mutable) : `키-값`들의 모음

### **`시퀀스형 주요 공통 연산자`**

|연산|결과|
|--|--|
|s[i]|s의 i번쨰 항목, 0에서 시작합니다.|
|s[i:j]|s의 i에서 j까지의 슬라이스|
|`s[i:j:k]`|`s의 i에서 j까지 스텝 k의 슬라이스`|
|s + t|s와 t의 이어붙이기|
|s * n or n * s|s를 그 자신에 n번 더하는 것|
|`x in s`|`s의 항목 중 하나가 x와 같으면 True, 그렇지 않으면 False`|
|x not in s|s의 항목 중 하나가 x와 같으면 False, 그렇지 않으면 True|
|len(s)|s의 길이|
|min(s)|s의 가장 작은 항목|
|max(s)|s의 가장 큰 항목|


## **`문자열(String Type)`**
- 모든 문자는 str 타입
- 문자열은 작은 따옴표(')나 큰 따옴표(")를 표기
- 문자열 특징: `변경 불가능`, `반복 가능`
- 중첩따옴표
    - 따옴표 안에 따옴표를 표현할 경우

### 인덱싱
- 인덱스를 통해 특정 값에 접근할 수 있음
s[1] => 'b'

### 슬라이싱
s[2:5] => 'cde'


### 기타
- 결합(Concatenation)
- 반복(Repetition)

``` python
name = 'hi!' * 3
print(name) # hi!hi!hi!
```
- 포함(Membership)

### Escape sequence
- 문자열 내에서 특정 문자나 조작을 위해서 역슬래시(\)를 활용하여 구분

|예약문자|내용|
|--|--|
|\n|줄 바꿈|
|\t|탭|
|\r|캐리지리턴|
|\0|널(Null)|
|\\|\|
|\'|단일인용부호(')|
|\"|이중인용부호(")|

## **`리스트(List)`**
- 변경 가능한 값들의 나열된 자료형
- 순서를 가지며, 서로 다른 타입의 요소를 가질 수 있음
- `변경 가능`하며, `반복 가능`함
- 항상 대괄호 형태로 정의, 요소는 콤마로 구분
```
[0, 1, 2, 3, 4, 5]
```
- 리스트 값 추가와 삭제

## None
- 파이썬 자료형 중 하나
- 파이썬에서는 값이 없음을 표현하기 위해 None 타입이 존재함.
- 일반적으로 반환 값이 없는 함수에서 사용하기도 함.

## 코드 작성 주의 사항
- 대소문자 구분
- 띄어쓰기, 문장부호 등 주의 깊게 활용
- 들여쓰기(indetation)
    - 문장을 구분할 때, 들여쓰기 (Indentation)를 사용
    - 들여쓰기 할 때는 4칸 혹은 1탭을 입력

## 주석(Comment)
- 코드에 대한 설명

### 필수 단축기

- 파일 만들기 : ctrl + n (new)
- 파일 저장하기 : ctrl + s (save)
- 주석 처리하기 : ctrl + /

