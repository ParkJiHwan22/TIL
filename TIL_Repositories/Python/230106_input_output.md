# 파일 입출력

## 학습 목표

> 파이썬을 활용하여 파일을 읽고 쓸 수 있다.

> JSON 형식의 파일을 읽고 활용할 수 있다.

## 파일 입력
- open(file, mode='r', encoding=None)
    - file : 파일명, mode : 텍스트 모드, encoding : 인코딩 방식(일반적으로 utf-8)
    - **`r : reading, w : writing, a: appending`** 

### 파일 활용

- 파일 객체 활용

- with 키워드 활용
``` python
with open('workfile') as f:
    read data = f.read

# We can check that the file has been automatically closed.
f.closed
True
```

- with 키워드를 사용하지 않으면, f.close()를 반드시 호출하여 종료시켜야 오류가 발생하지 않음. 따라서 일반적으로 with 키워드를 활용하여 작성

## JSON
- JSON은 자바스크립트 객체 표기법으로 개발환경에서 많이 사용되는 데이터 양식으로 웹 어플리케이션에서 데이터를 전송할 때 일반적으로 사용함
- 문자 기반(텍스트)데이터 포멧으로 다수의 프로그래밍 환경에서 쉽게 활용 가능함
    - 텍스트를 언어별 데이터 타입으로 변환
    - 언어별 데이터 타입을 적절하게 텍스트로 변환

### JSON 파일의 활용
- 객체(리스트, 딕셔너리 등)를 JSON으로 변환
``` python
import json
x = [1, 'simple', 'list']
json.dumps(x)
'[1, "simple", "list"]'
```
- JSON을 객체(리스트, 딕셔너리 등)로 변환

``` python 
x = json.load(f)
```

### pprint
- 임의의 파이썬 데이터 구조를 예쁘게 인쇄할 수 있는 기능을 제공