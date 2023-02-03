# a = [1, 2, 3, 4, 5]
# # n == 1 : [2, 3, 4, 5, 1]
# # n == 2 : [3, 4, 5, 1, 2]

# N = len(a)
# m = 3
# new_a = [None for _ in range(N)]
# print(a, new_a)

# for i in range(N):
#     new_a[(i+m)%N] = a[i]
#     print(new_a)


# from collections import deque

# a = [1, 2, 3, 4, 5]
# d = deque(a)
# d.rotate(2)
# d.rotate(-2)
# print(d)




# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 0, 1, 2]
# ]

# N = len(matrix)
# M = len(matrix[0])

# for i in range(M):
#     count = 0
#     for j in range(N):
#         count += matrix[j][i]
#     print(count)





# first_array = [list(map(int, input().split())) for _ in range(2)]
# second_array = [list(map(int, input().split())) for _ in range(2)]

# for i in range(2):
#     for j in range(3):
#         print(first_array[i][j] * second_array[i][j], end = ' ')
#     print()



# # 전치(transpose)

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 0, 1, 2]
# ]

# transported_matrix = [[0] * 3 for _ in range(4)]

# for i in range(4):
#     for j in range(3):
#         transported_matrix[i][j] = matrix[j][i]
# print(transported_matrix)



# # 회전
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# n = 3
# rotated_matrix = [[] * n for _ in range(n)]

# for i in range(n):
#     for j in range(n):
#         rotated_matrix[i][j] = matrix[n-j-1][i]


# zip 사용법

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(list(zip(*matrix)))
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

print(list(zip(*matrix[::-1])))
#[(7, 4, 1), (8, 5, 2), (9, 6, 3)]