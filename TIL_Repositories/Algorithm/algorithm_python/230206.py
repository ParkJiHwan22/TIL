graph = [
    [1, 2],
    [0, 3, 4],
    [0, 4, 5],
    [1],
    [1, 2, 6],
    [2],
    [4]
]

visited = [False] * n # 방문 처리 리스트 만들기

def dfs(start):
    stack = [start]  # 돌아갈 곳을 기록
    visited[start] = True  # 시작 정점 방문 처리

    while stack:  # 스택이 빌 때까지(돌아갈 곳이 없을 때까지) 반복
        cur = stack.pop()  # 현재 방문 정점(후입선출)

        for adj in graph[cur]:  # 인접한 모든 정점에 대해
            if not visited[adj]:  # 아직 방문하지 않았다면
                visited[adj] = True  # 방문 처리
                stack.append(adj)  # 스택에 넣기

dfs(0)  # 0번 정점에서 시작