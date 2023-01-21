# 음료수 얼려 먹기: 답안 예시 (Python)

# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m: # 주어진 범위를 벗어나는 경우에는 즉시 종료
        return False
    if graph[x][y] == 0: # 현재 노드를 아직 방문하지 않았다면
        graph[x][y] = 1 # 해당 노드 방문 처리
        dfs(x - 1, y) # 상하좌우 위치들도 모두 재귀적으로 호출
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

n, m = map(int, input().split()) # n, m을 공백을 기준으로 구분하여 입력 받기
graph = [] # 2차원 리스트의 맵 정보 입력 받기
for i in range(n):
    graph.append(list(map(int, input())))

result = 0
for i in range(n):
    for j in range(m): # 현재 위치에서 DFS 실행
        if dfs(i, j) == True:
            result += 1

print(result) # 정답 출력