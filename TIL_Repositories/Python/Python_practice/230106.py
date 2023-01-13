
file = open('test.txt', 'r', encoding='UTF8')
# # text = file.read()
# # print(text)
# text_2 = file.readline()
# print(text_2)
# text_2 = file.readline()
# print(text_2)
# text_2 = file.readline()
# print(text_2)
# file.close()

with open('test.txt', 'r', encoding='UTF8') as f:
    print(type(f))
    text_2 = file.readline()
    print(text_2)
    text_2 = file.readline()
    print(text_2)
    text_2 = file.readline()
    print(text_2)

# 파일을 가져다가 쓰고 싶을 때

import json
from pprint import pprint # key-value로 print 해줌
with open('data/movie.json', 'r', encoding='UTF8') as f:
    movie = json.load(f) # type 을 바뀌줌
    print(movie) 
    print(type(movie)) # <class 'dict'>
    print(movie['title']) # 영화 제목, 값 구하기

with open('data/movie.json', 'r', encoding='UTF8') as f:
    movie = json.load(f) # type 을 바뀌줌
    # pprint(movie)
    print(type(movie)) # <class 'dict'>
    # 각 리스트 요소?
    print(movie[0])