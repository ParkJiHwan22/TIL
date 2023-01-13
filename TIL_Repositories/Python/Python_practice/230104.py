'''
# 1부터 사용자가 입력한 양의 정수까지의 총합

#  n = int(input())
# sum = 0
# count = 0

# while n > count:

#     sum += count + 1
#     count += 1
 
# print(sum)

# n = int(input())
# sum = 0

# for i in range(1,n):
#     sum += sum + 1

# print(sum)

# print(*objects)
# *objects : *은 여러 값을 무한하게 받을 수 있다.
print('hi')
print('hi', 'hello')
print('hi', 'hello', 'guten tag')

# print(sep=' ', end='\n')
# sep=' ' : sep라는 키워드는 기본 값이 space
# end='\n' : end 라는 키워드는 기본 값이 개행
print('hi', 'hello', sep='!')
print('hi', end='')
print('hello')

# 함수의 반환 값(return)

# print 함수는 반환 값이 없습니다.
print('hi') # None

# sum 함수는 합을 반환합니다.
sum([1, 2, 3])

numbers = [10, 20, 5]

# 함수 객체
# 함수는 그 자체로 객체이다!
print(len)
print(type(len))
'''
# 함수 호출
# Input을 넣어서 함수를 실행시켰다!
print(len([1, 2, 3]))

# map 함수
# 첫번째 인자(Input)으로 함수를 받아서
# 두번째 인자(Input)인 반복 가능한 객체의 모든 요소에 적용!
a = ['1', '2', '3']
a = map(int, a)
print(sum(a))
