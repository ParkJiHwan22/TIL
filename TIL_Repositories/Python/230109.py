# List 내 중복 줄이기

# result = divmod(4,3)
# print(result)
# print(type(result))

# my_dict = {'name': '더 글로리', 'cast': '송혜교'}
# print(my_dict.keys())
# print(type(my_dict.items()))

# for a in my_dict.items():
#     print(a)
#     print(type(a))

# my_list = ['서울', '서울', '대전', '광주', '서울', '대전', '부산', '부산']

# # my_list = set(my_list)
# # print(my_list)

# new_list = []

# for i in my_list:
#     if i in new_list:
#         continue
#     else:
#         new_list.append(i)

# print(new_list)



# join method 사용법

# result = ['1', '5', '3']

# # 153을 출력해야 한다...?

# # (1) print의 키워드를 써서 출력
# # (2) 반복하면서 문자열을 만들음

# text = ''
# for elem in result:
#     text = text + elem
# print(text)

# # (2-2) join 메서드
# print(''.join(result))

# # 1 5 3 4
# print(' '.join(result))


# # 뒤집기

# text = 'hello'
# print(text[::-1])
# numbers = [3, 2, 10]
# print(numbers[::-1])


# # get 함수 사용법
# drama = {'name': '더 글로리', 'writer': '김은숙'}
# print(drama['name'])
# # print(drama['director'])
# print(drama.get('director')) # None


# students = {'홍엽' : 89, '민지' : 20, '소담' : 47}
# print(students['홍엽'])
# print(students.get('길동', 0))



# 지역별 개수 구하기
locations = ['서울', '서울', '대전', '광주', '서울', '대전', '부산', '부산']
result = {}
for location in locations:
    # 만약에 result에 있으면 값 추가
    if location in result:
        result[location] += 1
    # 만약에 result에 없으면 키 값 추가
    else:
        result[location] = 1
print(result)

result = {}
for location in locations:
    # 만약에 result에 있으면 값 추가
    # if location in result:
    result[location] = result.get(location, 0) + 1

print(result)