# 백트래킹(Backtracking)

### 백트래킹 기법
- 어떤 노드의 유망성을 점검한 후에 유망하지 않다고 결정되면 그 노드의 부모로 되돌아가 다음 자식 노드로 감

- 어떤 노드를 방문하였을 때 그 노드로 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 하여, 반대로 해답의 가능성이 있으면 유망하다고 함

- 가지치기(pruning): 유망하지 않는 노드가 포함되는 경로는 더 이상 고려하지 않음

### 백트래킹과 깊이 우선 탐색과의 차이
- 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임 (Prunning 가지치기)
- 깊이 우선 탐색이 모든 경로를 추적하는데 비해 백트래킹은 불필요한 경로를 조기에 차단
- 깊이 우선 탐색을 가하기에는 경우의 수가 너무나 많음, 즉 N! 가지의 경우의 수를 가진 문제에 대해 깊이 우선 탐색을 가하면 당연히 처리 불가능한 문제
- `백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우에는 여전히 지수함수시간(Exponential Time)을 요하므로 처리 불가능`

### 백트래킹을 이용한 알고리즘은 다음과 같은 절차로 진행
1. 상태공간 트리의 깊이 우선 탐색을 실시
2. 각 노드가 유망한지를 점검
3. 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색을 계속함

### 백트래킹 알고리즘

checknode (node v)
    IF promising( v )
        IF there is a solution at v
            write the solution
        ELSE
            FOR each child u of v
                checknode( u )

# 순열 (Permutation)