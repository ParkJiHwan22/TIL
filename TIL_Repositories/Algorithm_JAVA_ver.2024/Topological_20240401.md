# 위상 정렬(Topological Sorting)

### 위상 정렬이란?
- `순서가 있는 작업`을 차례로 진행해야 할 때 순서를 결정해 주기 위해 사용하는 알고리즘
- `사이클 없는 방향 그래프`의 모든 노드를 주어진 방향성에 어긋나지 않게 순서를 나열하는 것

- 위상정렬은 답이 여러가지가 나올 수 있다.

### DAG(Directed Acyclic Graph, 유향 비사이클 그래프)

- 진입 차수: 특정 노드로 들어오는 간선의 개수
- 진출 차수: 특정 노드에서 나가는 간선의 개수

### 위상 정렬 방법(Queue 사용)
1. 진입 차수가 0인 모든 노드를 Queue에 삽입
2. Queue가 공백상태가 될 때까지 반복 수행
    - Queue에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거한다(연결된 노드의 진입 차수를 감소시킨다.)
    - 새롭게 진입 차수가 0이 된 노드를 Queue에 삽입한다.

- Queue에서 꺼내지는 순서 (Queue에 들어오는 순서)가 정렬을 수행한 결과

### 위상 정렬 특징
- 모든 정점을 방문하기 전에 Queue가 공백 상태가 되면 사이클이 존재하는 것이다.(사이클이 존재하면 진입차수가 0이 될 수가 없음)
- 그래프의 유형은 DAG
- 여러 해답이 존재할 수 있다.(진입 차수가 0인 값이 동시에 생성이 된다면 작성한 코드 방법에 따라 달라진다.)
- 시간 복잡도 O(V + E)