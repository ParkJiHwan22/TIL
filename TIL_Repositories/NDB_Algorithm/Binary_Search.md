## 이진 탐색 알고리즘
- 순차 탐색 : 리스트 안에 있는 특정한 `데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인`하는 방법
- 이진 탐색 : 정렬되어 있는 리스트에서 `탐색 범위를 절반씩 좁혀가며 데이터를 탐색`하는 방법
    - 이진 탐색은 시작점, 끝점, 중간점을 이용해서 탐색 범위를 설정

### 이진 탐색의 시간 복잡도
- 단계마다 탐색 범위를 2로 나누는 것과 동일하므로 연산 횟수는 **`log₂N에 비례`**
- 이진 탐색은 탐색 범위를 절반씩 줄이며, 시간 복잡도는 O(logN)을 보장

``` python
# 이진 탐색 소스 코드 구현 (재귀함수)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split())) # 10 7
# 전체 원소 입력 받기
array = list(map(int, input().split())) # 1 3 5 7 9 11 13 15 17 19

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1) # 4
```

``` python
# 이진 탐색 소스 코드 구현 (반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split())) # 10 7
# 전체 원소 입력 받기
array = list(map(int, input().split())) # 1 3 5 7 9 11 13 15 17 19

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1) # 4
```

### 파이썬 이진 탐색 라이브러리
- bisect_left(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
- bisect_right(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환

``` python
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4
print(bisect_left(a, x)) # 2
print(bisect_right(a, x)) # 4
```

``` python
# 파이썬 이진 탐색 라이브러리
from bisect import bisect_left, bisect_right

# 값이 [left_index, right_index]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 배열 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))
```

### 파라메트릭 서치(Parametic Search)
- `파라메트릭 서치`란 `최적화 문제를 결정 문제로 바꾸어 해결하는 기법`
- 일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 **`이진 탐색을 이용하여 해결할 수 있음`**
