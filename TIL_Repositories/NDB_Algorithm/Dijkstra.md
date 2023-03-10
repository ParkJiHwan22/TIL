## 최단 경로 알고리즘
- 최단 경로 알고리즘은 '가장 짧은 경로를 찾는 알고리즘`
- **다양한 문제 상황**
    - 한 지점에서 다른 한 지점까지의 최단 경로
    - 한 지점에서 다른 모든 지점까지의 최단 경로
    - 모든 지점에서 다른 모든 지점까지의 최단 경로
- 각 지점은 그래프에서 `노드`로 표현
- 지점 간 연결된 도로는 그래프에서 `간선`으로 표현

## 다익스트라 최단 경로 알고리즘
- `특정한 노드`에서 출발하여 `다른 모든 노드`로 가는 최단 경로를 계산
- 음의 간선이 없을 때 정상적으로 동작
    - 현실 세계의 도로(간선)은 음의 간선으로 표현되지 않음
- 다익스트라 최단 경로 알고리즘은 그리디 알고리즘으로 분류
    - 매 상황에서 가장 비용이 적은 노드를 선택해 임의의 과정을 반복
- 알고리즘 동작 과정에서 최단 거리 테이블은 각 노드에 대한 현재까지의 최단 거리 정보를 가지고 있음

### 알고리즘의 `동작 과정`

1. 출발 노드를 설정
2. 최단 거리 테이블을 초기화
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
5. 3~4번 과정 반복

### 다익스트라 알고리즘의 특징
- 그리디 알고리즘: `매 상황에서 방문하지 않은 가장 비용이 적은 노드를 선택`해 임의의 과정을 반복
- 단계를 거치며 **`한 번 처리된 노드의 최단 거리는 고정`** 되어 더 이상 바뀌지 않음
- `한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해`할 수 있음
- 다익스트라 알고리즘을 수행한 뒤에 테이블에 각 노드까지의 최단 거리 정보가 저장됨
- 완벽한 형태의 최단 경로를 구하려면 소스코드에 추가적인 기능을 더 넣어야 함

### 다익스트라 알고리즘: 간단한 구현 방법
- 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 매 단계마다 1차원 테이블의 모든 원소를 확인(순차 탐색)

### 다익스트라 알고리즘: 간단한 구현 방법 성능 분석
- 총 O(V)번에 걸쳐서 최단 거리가 가장 짧은 노드를 매번 선형 탐색해야 함
- 따라서 전체 시간 복잡도는 O(V²)
- 5000개 이하의 노드는 문제 해결 가능


## 우선순위 큐(Priority Queue)
- `우선순위가 가장 높은 데이터를 가장 먼저 삭제`하는 자료구조
- 여러 개의 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건 데이터부터 꺼내서 확인해야 하는 경우에 우선순위 큐를 이용할 수 있음
- Python 에서 표준 라이브러리 형태로 지원

|자료구조|추출되는 데이터|
|--|--|
|스택(Stack)|가장 나중에 삽입된 데이터|
|큐(Queue)|가장 먼저 삽입된 데이터|
|우선순위 큐(Priority Queue)|가장 우선순위가 높은 데이터|

## 힙(Heap)
- `우선순위 큐(Priority Queue)를 구현하기 위해 사용하는 자료구조 중 하나`
- **최소 힙(Min Heap)** 과 **최대 힙(Max Heap)** 이 있음
- 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 사용됨

    |우선순위 큐 구현 방식|삽입 시간|삭제 시간|
    |--|--|--|
    |리스트|O(1)|O(N)|
    |힙(Heap)|O(logN)|O(logN)|

### 다익스트라 알고리즘: 개선된 구현 방법
- 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 `힙(Heap)자료구조`를 이용
- 다익스트라 알고리즘이 동작하는 `기본 원리는 동일`
    - 현재 가장 가까운 노드를 저장해 놓기 위해서 힙 자료구조가 추가적으로 이용한다는 점이 다름
    - 현재의 최단거리가 가장 짧은 노드를 선택해야 하므로 최소 힙을 사용

### 다익스트라 알고리즘: 개선된 구현 방법
- 힙 자료구조를 이용하는 다익스트라 알고리즘의 시간 복잡도는 **`O(ElogV)`**
- 노드를 하나씩 꺼내 검사하는 반복문(while문)은 노드의 개수 V이상의 횟수로는 처리되지 않음
    - 결과적으로 현재 우선순위 큐에서 꺼낸 노드와 연결된 다른 노드들을 확인하는 총횟수는 최대 간선의 개수(E)만큼 연산이 수행될 수 있음
- 직관적으로 `전체 과정은 E개의 원소를 우선순위 큐에 넣었다가 모두 빼내는 연산과 매우 유사`
- 시간 복잡도를 O(ElogE)로 판단할 수 있음
- 중복 간선을 포함하지 않는 경우에 이를 O(ElogV)로 정리할 수 있음
    - O(ElogE) -> O(ElogV²) -> O(2ElogV) -> O(ElogV)