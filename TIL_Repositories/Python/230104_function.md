# Python 기초 - 함수

## <학습목표>

> 함수를 사용해야 하는 이유를 알고 설명할 수 있다.

> 파이썬 내장 함수를 활용하여 코드를 작성할 수 있다.

> 함수별 인자와 return(반환)을 구분할 수 있다.


## <복습>
- for문 활용법
    1. 반복가능한 객체 `요소`
    2. range `index`

## While
- while문은 조건식이 참인 경우 반복적으로 코드를 실행
- 종료조건에 해당하는 코드를 통해 반복문을 종료시켜야 함
```  python
while <expression>:
    # Code block
```

## 함수(function)
- 왜 사용할까? : Abstraction(추상)
    - 복잡한 내용을 숨기고, 기능에 집중하여 사용할 수 있음(블랙박스), 재사용성, 가독성, 생산성
- input() → f(x) → output()
- `특정한 기능을 하는 코드의 조각(묶음)`
- 특정 명령을 수행하는 코드를 매번 다시 작성하지 않고, 필요 시에만 호출하여 간편히 사용

### 함수의 정의
- 사용자 함수(Custom Function) : 구현되어 있는 함수가 없는 경우, 사용자가 직접 함수를 작성 가능
``` python
def function_name
    # code block
    return returning_value
```
### 함수 기본 구조
- 선언과 호출(define & call)
- 입력(Input)
- 범위(Scope)
- 결과값(Output)

``` python
# print(*objects)
# *objects : *은 여러 값을 무한하게 받을 수 있다.
print('hi')
print('hi', 'hello')
print('hi', 'hello', 'guten tag')

# print(sep=' ', end='\n')
# sep=' ' : sep라는 키워드는 기본 값이 space
# end='\n' : end 라는 키워드는 기본 값이 개행
print('hi', 'hello', sep='!')
print('hi', end='')
print('hello')
```