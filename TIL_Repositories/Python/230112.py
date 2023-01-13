# import random

# # numbers = range(1, 46)
# # lucky = sorted(random.sample(numbers, 6))
# # print(lucky)

# def get_lotto(n):
#     # Input :
#     # n 로또 번호 세트 수
#     # Output :
#     # 오늘 지른 로또 금액
#     # 번호
#     result = []
#     for i in range(n):
#         result.append(sorted(random.sample(range(1, 46), 6)))
#     return n*1000, result

# def get_lotto_price(n):
#     return n*1000

# NUM_OF_LOTTO = 2
# print(get_lotto(2))
# print(get_lotto_price(2))

# ==================================
# Data :
    # N : 세트 수
    # Lotto 번호
# 기능 :
     # 로또 구매 금액 계산

# lst = []

# for i in range(1, 4):
#     lst.append(i**3)

# print(lst)

# [number**3 for number in range(1,4)]

A, B = map(int, input().split())
print(A+B, A-B, A*B, A//B, sep='\n')