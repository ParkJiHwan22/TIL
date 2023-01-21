# 딕셔너리 (Dictionary)

## 학습 목표

> 리스트와 딕셔너리의 특징과 시간 복잡도를 비교할 수 있다.

> 딕셔너리를 사용해야 하는 문제를 판별할 수 있다.

> 딕셔너리에 값을 추가, 삭제, 수정, 조회할 수 있다.

> 딕셔너리 주요 메서드를 활용할 수 있다.

## 1. 해시 테이블
- 파이썬에는 딕셔너리(dict) 자료구조가 내장 되어 있음
- `해시 함수`: 임의 길이의 데이터를 고정 길이의 데이터로 매핑하는 함수
- `해시` : 해시 함수를 통해 얻어진 값

### 파이썬 딕셔너리(Dictionary의 특징)
- 해시 함수와 해시 테이블을 이용하기 때문에 삽입, 삭제, 수정, 조회의 `연산의 속도가 리스트보다 빠름`
- Hash function을 이용한 산술 계산으로 값이 있는 위치를 바로 알 수 있기 때문
- 딕셔너리의 시간복잡도는 O(1)

### 딕셔너리는 언제 사용해야할까?
1. Key, Value 구조로 관리를 해야 하는 경우(순서나 인덱스가 아닌 경우)
2. 데이터에 대한 빠른 접근 탐색이 필요한 경우

## 2. 딕셔너리 기본 문법
- 선언 : 변수 = {key1:value1, key2:value2 ...}
- 삽입/수정 : 딕셔너리[key]=value
- 삭제 : 딕셔너리.pop(key.default)
- 조회 : 딕셔너리[key], 딕셔너리.get(key.default)

## 3. 딕셔너리 메서드

1. .keys()
2. .values()
3. .items()

``` python
my_dict = {
    'name' : 'tak',
    'role' : 'teacher'
}

print(my_dict) # {'name': 'tak', 'role': 'teacher'}
print(my_dict.get('age', 0)) # 0
print(my_dict.keys()) # dict_keys(['name', 'role'])
print(my_dict.values()) # dict_values(['tak', 'teacher'])
print(my_dict.items()) # dict_items([('name', 'tak'), ('role', 'teacher')])
```

### **Input 대체**

``` python
members = [
    "Jay", "John", "John", "Jay", "Jack", "Jack", "John", "Jo", "Jo", "Jack"
]

count = {} 

for member in members:
    # if member in count:
    #     count[member] = count[member] + 1
    # else:
    #     count[member] = 1
    count[member] = count.get(member, 0) + 1
    
count_items = count.items()
print(count_items) # dict_items([('Jay', 2), ('John', 3), ('Jack', 3), ('Jo', 2)])

from collections import Counter 
new_count_items = Counter(members)
print(new_count_items) # Counter({'John': 3, 'Jack': 3, 'Jay': 2, 'Jo': 2})
```



``` python
from collections import Counter 

print(Counter('pen pineapple apple pen'))
print(Counter('pen pineapple apple pen').most_common())
print(Counter('pen pineapple apple pen').most_common(2))
```