# Python 기초 - 컬렉션(Collections)

## <학습목표>

> 딕셔너리의 특징을 이해하고 다른 데이터 타입과 비교할 수 있다.

> 딕셔너리 키 접근을 할 수 있고, 값을 추가할 수 있다.

> 딕셔너리 순회의 결과를 설명할 수 있다.

## 딕셔너리(Dictionary)
- `키-값(key-value) 쌍으로 이뤄진 모음(collection)`
- 키(key)
    - 불변 자료형만 가능(list, dictionary는 불가능)
- 값(values)
    - 어떠한 형태든 관계 없음
- 키와 값은 `:` 로 구분 됩니다. 개별 요소는 `,`로 구분 됩니다.
- 변경 가능하며(mutable), 반복 가능함(iterable)
    - 딕셔너리는 반복하면 키가 반환됩니다.

### 딕셔너리(Dictionary) 생성
- key와 value가 쌍으로 이뤄진 자료구조
    - key는 변경 불가능한 데이터(immutable)만 활용 가능
    - str, int, float, bool, tuple, range
    - value는 모든 값으로 설정 가능(List, Dictionary 등)

### 딕셔너리(Dictionary)  키-값 추가 및 변경
- 딕셔너리에 키와 값의 쌍을 추가할 수 있으며,
- 이미 해당하는 키가 있다면 기존 값이 변경됨
``` python
pokemon = {'피카츄' : '전기', '이상해씨' : '풀', '꼬부기' : '물'}
pokemon['이상해씨'] = 불
# {'피카츄' : '전기', '이상해씨' : '불', '꼬부기' : '물'}
pokemon['꼬부기'] = 바위
# {'피카츄' : '전기', '이상해씨' : '불', '꼬부기' : '바위'}
```

### 딕셔너리(Dictionary)  키-값 삭제
- 키를 삭제하고자하면 .pop을 활용하여 삭제하고자 하는 키를 전달
- 키가 없는 경우는 KeyyError 발생

### `딕셔너리 순회`
- 딕셔너리는 기본적으로 key를 순회하며, key값을 활용
- 추가 메서드를 활용하여 순회할 수 있음
    - dict_keys() : key로 구성된 결과
    - dict_values() : value로 구성된 결과
    - dict_items() : (Key, value)의 튜플로 구성된 결과



# 모듈
## <학습목표>

> 파이썬 내장 라이브러리 문서를 읽고 활용할 수 있다.

> random, datetime 모듈을 활용하여 코드를 작성할 수 있다.

> 패키지를 설치하고 패키지 목록을 관리할 수 있다.

- `(모듈, module)` : 다양한 `기능`을 하나의 `파일`로
- `(패키지, package)` : 다양한 `파일`을 하나의 `폴더`로
- `(라이브러리, library)` : 다양한 `패키지`를 하나의 `묶음`으로

- `pip`: 위의 `모든 것을 관리`하는 관리자 

### 모듈과 패키지
- 모듈
    - 특정 기능을 하는 코드를 파이썬(.py) 단위로 작성한 것
- 패키지
    - 특정 기능과 관련된 여러 모듈의 집합
    - 패키지 안에는 또 다른 서브 패키지를 포함

## 파이썬 표준 라이브러리(PSL)
- 파이썬에 기본적으로 설치된 모듈과 내장 함수

### random
- 숫자/수학 모듈 중 의사 난수 생성(pseudo random number generator)
    - 대표적으로 임의의 숫자 생성, 무작위 요소의 선택, 무작위 비복원 추출을 위한 함수 제공
- random.randint(a,b)
    - a이상  b이하의 임의의 정수 N을 반환
- random.choice(seq)
    - 비어 있지 않은 시퀀스에서 임의의 요소를 반환
    - seq가 비어있으면 IndexError를 발생시킴
- random.shuffle(seq)
    - 시퀀스를 제자리에서 섞습니다.
- random.sample(population, k)
    - 무작위 비복원 추출의 결과인 k 길이의 리스트를 반환합니다.

### datetime
- 날짜와 시간을 조작하는 객체를 제공
- 사용 가능한 데이터 타입
    - datetime.date, datetime.time, datetime.datetime, datetime.timedelta 등
- datetime.date(year, month, day)
    - 모든 인자가 필수입니다. 인자는 특정 범위에 있는 정수이어야 함
    - 이 범위를 벗어나는 인자가 주어지면 ValueError가 발생함
- datetime.date.today()
    - 현재 지역 날짜를 반환합니다.
- datetime.datetime.today()
    - 현재 지역 datetime을 반환합니다. now()를 활용하면 타임존을 설정할 수 있습니다.

### OS
- OS(운영체제)를 조작하기 위한 인터페이스 제공
- os.listdir(path='.')
    - path에 의해 주어진 디렉터리에 있는 항목들의 이름을 담고 있는 리스트를 반환함
    - 리스트는 임의의 순서로 나열되며, 특수문자는 포함하지 않음
- os.mkdir(path)
    - path라는 디렉터리를 만들음
- os.chdir(path)
    - path를 변경함






## 파이썬 패키지 관리자(pip)
- PyPI(Python Package Index)에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템