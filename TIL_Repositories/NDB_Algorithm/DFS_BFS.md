## DFS(Depth-First Search)
- DFS는 `깊이 우선 탐색`이라고도 부르며 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
- DFS는 `스택 자료구조(혹은 재귀 함수)를 이용`
- 구체적인 동작 과정
    1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
    2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
    3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복

## BFS(Breadth-First Search)
- BFS는 `너비 우선 탐색`이라고도 부르며, 그래프에서 `가까운 노드부터 우선적으로 탐색하는 알고리즘`
- BFS는 `큐 자료구조`를 이용
- 구체적인 동작 과정
    1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 함
    2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
    3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복