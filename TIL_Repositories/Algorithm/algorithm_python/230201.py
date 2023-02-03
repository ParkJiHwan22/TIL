# 블랙잭

# from itertools import combinations

# n, m = map(int, input().split())
# num_list = list(map(int, input().split()))

# t = sum(combinations(num_list, 3))



x = 0
y = 0

# 1. 델타값 정의(상하좌우)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 2. 이차원 리스트 순회
for x in range(n):
    for y in range(m):

        # 1. 델타값을 이용해 상하좌우 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 2. 범위를 벗어나지 않으면 갱신
            if 0 <= nx < 3 and 0 <= ny < 3:
                x = nx
                y = ny
