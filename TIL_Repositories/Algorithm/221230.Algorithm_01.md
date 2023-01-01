# 최적의 코딩을 결정하는 기본 알고리즘

## 스택 자료구조 (상자쌓기, 프링글스통)
- 먼저 들어온 데이터가 나중에 나가는 형식(선입후출)의 자료구조
- `입구와 출구가 동일한 형태`로 스택을 시각화할 수 있다.
- 삽입과 삭제의 두 연산으로 구성됨

### 스택 구현 예제 (Python)
``` python
stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력
print(stack) # 최하단 원소부터 출력
```

## 큐 자료구조 (터널, 대기열)
- 먼저 들어온 데이터가 먼저 나가는 형식(선입선출)의 자료구조
- 큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화 할 수 있다.

### 큐 구현 예제 (Python)
``` python
from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 순서대로 출력
```
## 우선순위 큐(Priority Queue)
 - 우선순위 큐는 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조이다.
 - 우선순위 큐는 데이터를 우선순위에 따라 처리하고 싶을 때 사용한다.
    - 예시) 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건부터 꺼내서 확인해야 하는 경우

|자료구조|추출되는 데이터|
|--|--|
|스택(Stack)|가장 나중에 삽입된 데이터|
|큐(Queue)|가장 먼저 삽입된 데이터|
|우선순위 큐(Priority Queue)|가장 우선순위가 높은 데이터|

### 우선순위 큐를 구현하는 방법
1. 단순히 리스트를 이용하여 구현한다.
2. 힙(heap)을 이용하여 구현한다.
- 데이터의 개수가 N개일 때, 구현 방식에 따라서 시간 복잡도를 비교한 내용은 다음과 같다.

|우선순위 큐 구현 방식|삽입 시간|삭제 시간|
|--|--|--|
|리스트|O(1)|O(N)|
|힙(Heap)|O(logN)|O(logN)|

- 단순히 N개의 데이터를 힙에 넣었다가 모두 꺼내는 작업은 정렬과 동일함 (힙 정렬)
    - 이 경우 시간 복잡도는 O(NlogN)이다.
    
### 힙(Heap)의 특징
- 힙은 완전 이진 트리자료 구조의 일종이다.
- 힙에서는 항상 `루트 노드(root node)를 제거`한다.
- `최소 힙(min heap)`
    - 루트 노드가 가장 작은 값을 가진다.
    - 따라서 값이 가장 작은 데이터가 우선적으로 제거된다.
- `최대 힙(max heap)`
    - 루트 노드가 가장 큰 값을 가진다.
    - 따라서 값이 큰 데이터가 우선적으로 제거된다.

### 완전 이진 트리 (Complete Binary Tree)
- `완전 이진트리`란 루트(root)노드부터 시작하여 왼쪽 자식 노드, 오른쪽 자식 노드 순서대로 데이터가 차례대로 삽입되는 트리(tree)를 의미한다.

### 최소 힙 구성 함수: Min-Heapify()
- (상향식) 부모 노드로 거슬러 올라가며, 부모보다 자신의 값이 더 작은 경우에 위치를 교체한다.
- 힙에 새로운 원소가 삽입되었을 때 O(logN)의 시간 복잡도로 힙 성질을 유지하도록 할 수 있다.
- 힙에 원소가 제거되었을 때 O(logN)의 시간 복잡도로 힙 성질을 유지하도록 할 수 있다.
    - 이후에 루트 노드에서부터 하향식으로(더 작은 자식 노드로) Heapify()를 진행한다.

### 우선순위 큐 라이브러리를 활용한 힙 구현 예제 (Python)
``` python
import sys
import heapq
input = sys.stdin.readline

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

res = heapsort(arr)

for i in range(n):
    print(res[i])
```