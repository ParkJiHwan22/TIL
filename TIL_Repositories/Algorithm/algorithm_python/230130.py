# # 3x3
# matrix = [list(map(int, input().split())) for i in range(3)]
# print(matrix[0][0])

# # 1 2 3
# # 4 5 6
# # 7 8 9





# # 8x7
# n,m = map(int, input().split())
# matrix = []

# for _ in range(n):
#     line = list(map(int, input().split()))
#     matrix.append(line)

# # 8 7
# # 1 2 3 4 5 6 7
# # 1 2 3 4 5 6 7
# # 1 2 3 4 5 6 7
# # 1 2 3 4 5 6 7
# # 1 2 3 4 5 6 7
# # 1 2 3 4 5 6 7
# # 1 2 3 4 5 6 7
# # 1 2 3 4 5 6 7






# n = 4 # 행
# m = 3 # 열

# matrix1 = [[0] * m for _ in range(n)]
# matrix2 = [[0] * m] * n

# matrix1[0][0] = 1
# matrix2[0][0] = 1

# print(matrix1) # [[1, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
# print(matrix2) # [[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]





# # n x m 크기의 입력을 받아보자.

# n,m = map(int, input().split())
# num_list = [list(map(int, input().split())) for _ in range(n)]


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8], 
    [9, 0, 1, 2]
]

for i in range(3):
    for j in range(4):     
        matrix[i][j]

