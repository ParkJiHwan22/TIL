# 전화번호부
# 키 - 이름 {상호명}
# 값 - 전화번호
'''
phone_book ={
    '전화번호' : '114',
    '피자헛' : '1588-5588',
    '김탁희' : '010-1233-1233',
    '대리운전' : ['1577-1577', '2580-2580']
}
# print(phone_book) #
# print(phone_book['피자헛'])
# print(phone_book['대리운전'])

for name in phone_book: # name : 변수 이름
    # print(name) # 키 값만 출력
    print(phone_book[name]) # 값 순회
'''

# pokemon = {'피카츄' : '전기', '이상해씨' : '풀', '꼬부기' : '물'}
# pokemon['이상해씨'] = '불'
# for name in pokemon:
#     print(name, pokemon[name])
# # {'피카츄' : '전기', '이상해씨' : '불', '꼬부기' : '물'}
# pokemon['꼬부기'] = '바위'
# for name in pokemon:
#     print(name, pokemon[name])
# # {'피카츄' : '전기', '이상해씨' : '불', '꼬부기' : '바위'}

# # 1. 모듈을 가져오는 것!
# import random

# menu = ['햄버거', '국밥', '초밥']
# print(random.choice(menu))

# 로또 추첨 코드 작성
# random.sample(population, k)
# Return a k length list 6개 숫자
# the population sequence. 1~45개 숫자 중

# import random
# lotto_45 = []

# for i in range(1,46):
#     lotto_45.append(i)

# print(random.sample(lotto_45, 6))

import random

# numbers = range(1, 46)
# lucky_numbers = random.sample(numbers, 6)
# print(sorted(lucky_numbers))

# print(sorted(random.sample(range(1, 46), 6)))

# # .sort() : 메서드
# # return : None
# # 해당 리스트 자체를 정렬!
# numbers = [10, 2, 5]
# result = numbers.sort()
# print(result) # None
# print(numbers)

# numbers = [10, 2, 5]
# numbers.sort()
# print(numbers)

# # sorted() : 함수
# # return : 정렬된 리스트
# numbers = [10, 2, 5]
# numbers.sorted(numbers)
# print(result) # [2, 5, 10]

# students = ['민욱', '홍엽', '현석', '정은']
# print(students)
# random.shuffle(students)
# print(students)

import datetime

# print(datetime.datetime.now())
# print(datetime.date(2023, 1, 5))

# today = datetime.date(2023, 1, 5)
# print(today)
# print(type(today))
# print(today.year)
# print(today.month)
# print(today.day)

# end = datetime.date(2023, 6, 14)
# print(f'우리가 개발자가 되는 시간...{end - today}')

import os

# print(os.listdir())