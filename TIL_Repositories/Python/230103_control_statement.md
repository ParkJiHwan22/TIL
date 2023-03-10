# Python 기초 - 제어문

- 객체(Object)를 활용하기 위해 Type과 연산자가 중요

## <학습목표>

> `조건문`을 활용한 코드를 작성하고 문제 풀이에 적용할 수 있다.

> `반복문`을 활용한 코드를 작성하고 문제풀이에 적용할 수 있다.

> `for 반복문`과 `while 반복문`의 `차이를 비교`하고 사용할 수 있다.

> `중첩`된 조건문과 반복문의 결과를 판단할 수 있다.

> 반복문 제어를 활용하여 원하는 조건의 `반복 종료`를 실행시킬 수 있다.

## 제어문
- 파이썬은 기본적으로 위에서부터 아래로 순차적으로 명령을 수행
- 특정 상황에 따라 코드를 선택적으로 실행(분기/조건)하거나 계속하여 실행(반복)하는 제어가 필요함
- 제어문은 순서도(flow chart)로 표현이 가능

### 조건문
- 조건이 참인지 거짓인지에 따라 실행되는 코드가 다름.
``` python
if < expression >:
    # Run this block
elif < expression >:
    # Run this block
else:
    # Run this block
```

### 중첩조건문
- 조건문은 다른 조건문에 중첩되어 사용될 수 있음
    - 들여쓰기를 유의하여 작성할 것

## 레인지(Range)
- 숫자의 시퀀스를 나타내기 위해 사용
- 기본형 : range(n)
    - 0부터 n-1까지의 숫자의 시퀀스
- 범위 지정 : range(n, m)
    - n부터 m-1까지의 숫자의 시퀀스
- 범위 및 스텝 지정 : range(n, m, s)
    - n부터 m-1까지 s만큼의 간격으로 커지는 숫자의 시퀀스
- `변경 불가능`하며, `반복가능`함

## 반복문
- while 문 : 종료조건에 해당하는 코드를 통해 반복문을 종료시켜야 함
- for 문 : 반복가능한 객체를 모두 순회하면 종료(별도의 종료조건이 필요없음)
- 반복 제어 : break, continue, for-else

## for문
- for문은 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체(iterable)요소를 모두 순회함

### 문자열 순회
``` python

chars = input()

for char in chars: # for <변수명> in <iterable>
    print(char)
```

- 문자열 순회
``` python
chars = input()

for idx in range(len(chars)):
    print(chars[idx])
```

- 예시)
``` python
a = 'pineapple'
# pineapple => 0 ~ 8 len('pineapple')-1

# 1. 반복 가능한 객체 : 각 요소를 원할 때
for char in a:
    print(char)

# 2. 반복 가능한 객체 : 인덱스가 필요할 때
for i in range(len(a)):
    print(i,a[i])
```

### 반복문 제어
- break : 반복문을 종료
- continiue : continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행
- for-else : 끝까지 반복문을 실행한 이후에 else문 실행 : break를 통해 중간에 종료되는 경우 else 문은 실행되지 않음

- break, continue 예시)
``` python
word = 'banana'

# a가 있으면 1을 출력하고 종료하세요.
for char in word:
    if char == 'a':
        print(1)
        break

print('===========')
# a를 제외하고 모두 출력하세요.
# continue : 다음 반복을 실행
for char in word:
    if char == 'a':
        continue
    print(char)


for char in word:
    if char != 'a':
        print(char)
```

- for-else 예시)
``` python
word = 'emango'

# 'e' 있으면 1을 출력
# 'e' 없으면 0을 출력

is_end = False # T/F

for char in word:
    if char == 'e':
        print(1)
        is_end = True
        break
```