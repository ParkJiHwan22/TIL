# 에러 / 예외 처리 (Error/Exception Handling)
## <학습목표>

> 파이썬에서 발생하는 `에러메세지를 읽고 해석`할 수 있다.

> 에러메시지를 읽고 디버깅을 하여 코드의 문제를 해결할 수 있다.

> SW개발자 관점에서 예외를 처리하고 에러를 발생시키는 방법을 익힐 수 있다.

### 오류가 발생되는 시점
- 제어가 되는 시점 : 조건/반복, 함수
    - 값이 변경되는 시점

### 디버깅
- branches : 모든 조건이 원하는대로 동작하는지
- for loops : 반복문에 진입하는지, 원하는 횟수만큼 실행되는지
- while loops : for loops와 동일, 종료조건이 제대로 동작하는지
- function : 함수 호출시, 함수 파라미터, 함수 결과

## 문법 에러(Syntax Error)
- SyntaxError가 발생하면, 파이썬 프로그램은 실행이 되지 않음
- 파일이름, 줄번호, ^문자를 통해 파이썬이 코드를 읽어 나갈 때(parser)문제가 발생한 위치를 표현
- 줄에서 에러가 감지된 가장 앞의 위치를 가리키는 캐럿(caret)기호(^)를 표시
- EOL(End of Line)
- EOF (End of Fole)
- Invalid syntax
- assign to literal

### 예외(Exception)
- 실행도중 예상치 못한 상황을 맞이하면 , 프로그램 실행을 멈춤
    - 문장이나 표현식이 문법적으로 올바르더라도 발생하는 에러
    - 실행 중에 감지되는 에러들을 예외(Exception)라고 부름
    - 모든 내장 예외는 Exception Calss를 상속받아 이뤄짐
- ZeroDivision Error : 0으로 나누고자 할 때 발생
- NameError : namespace 상에 이름이 없는 경우
- TypeError : 타입 불일치
- ValueError : 타입은 올바르나 값이 적절하지 않거나 없는 경우
- 이외에도 IndexError, keyError, moduleNotFoundError, Import/Error, IndentationError, KeyboardInterrupt 등이 있음

## 예외처리
- try 문(statement) / except 절(clause)을 이용하여 예외 처리를 할 수 있음
- try문
    - 오류가 발생할 가능성이 있는 코드를 실행
    - 예외가 발생되지 않으면, except 없이 실행 종료
- except문
    - 예외가 발생하면, except절이 실행
    - 예외 상황을 처리하는 코드을 받아서 적절한 조치를 취함
``` python
try:
    except 예외그룹-1 as 변수-1 :
        예외처리 명령문 1
    except 예외그룹-2 as 변수-2 :
        예외처리 명령문 2
    finally: # 여기서부터는 선택사항
        finally 명령문
```
