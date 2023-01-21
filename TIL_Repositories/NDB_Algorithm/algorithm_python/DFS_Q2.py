from collections import deque

n, m = map(int, input().split()) # n, m을 공백을 기준으로 구분하여 입력 받기
graph = [] # 2차원 리스트의 맵 정보 입력 받기
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0] # 이동할 네 가지 방향 정의 (좌, 우, 하, 상)
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    queue = deque() # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue.append((x, y))

    while queue: # 큐가 빌 때까지 반복하기
        x, y = queue.popleft()  # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m: # 마로 찾기 공간을 벗어난 경우 무시
                continue
            if graph[nx][ny] == 0: # 벽인 경우 무시
                continue
            if graph[nx][ny] == 1: # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1] # 가장 오른쪽 아래까지의 최단 거리 반환


print(bfs(0, 0)) # BFS를 수행한 결과 출력
