# name = '하니'
# age = 19.9

# print(name = '는 ' + str(age) + '살입니다.')
# print('{}는 {}살입니다.'.format(name, age))
# print(f'{name}는 {age}살입니다.')

# if 5 > 3:
#     print('크다!')
# else:
#     print('작다!')

# num = input()
# if int(num) == 0:
#     print("0")
# elif int(num) % 2 == 1:
#     print("홀수")
# else:
#     print("짝수")

# dust = input()

# if int(dust) > 150 :
#     print("매우 나쁨")
# elif int(dust) > 80 :
#     print("나쁨")
# elif int(dust) > 30 :
#     print("보통")
# else:
#     print("좋음")

# a = range(1,11,3)
# print(a) # range(0, 4)
# print(list(a))

# a = 'apple'

# for char in a:
#     print(char)

# l =['윤원','용진','필진']

# for name in l:
#     print(name)

# for num in range(3):
#     print(num**2)

# a = 'pineapple'
# # pineapple => 0 ~ 8 len('pineapple')-1

# # 1. 반복 가능한 객체 : 각 요소를 원할 때
# for char in a:
#     print(char)

# # 2. 반복 가능한 객체 : 인덱스가 필요할 때
# for i in range(len(a)):
#     print(i,a[i])

# word = 'banana'

# # a가 있으면 1을 출력
# for char in word:
#     # print(char)
#     if char == 'a':
#         print(1)

# print('===========')
# if 'a' in word:
#     print(1)

# word = 'banana'

# # a가 있으면 1을 출력하고 종료하세요.
# for char in word:
#     if char == 'a':
#         print(1)
#         break

# print('===========')
# # a를 제외하고 모두 출력하세요.
# # continue : 다음 반복을 실행
# for char in word:
#     if char == 'a':
#         continue
#     print(char)


# for char in word:
#     if char != 'a':
#         print(char)     

word = 'emango'

# 'e' 있으면 1을 출력
# 'e' 없으면 0을 출력


is_end = False # T/F

for char in word:
    if char == 'e':
        print(1)
        is_end = True
        break