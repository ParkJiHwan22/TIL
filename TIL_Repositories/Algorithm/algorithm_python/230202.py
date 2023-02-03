N = 7
M = 7 # input 수이면서 간선의 개수
graph = []

graph = [[0]*N for _ in range(N)]
print(graph)


for i in range(N):
   v1, v2 = map(int, input().split())
   graph[v1][v2] = 1
   graph[v2][v1] = 1

print(graph)