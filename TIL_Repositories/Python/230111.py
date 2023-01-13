# class Person:

#     def greeting(self):
#         return 'hi....'

# iu = Person() # 인스턴스 생성
# jimin = Person() # 인스턴스 생성

# # Person 타입을 가짐
# print(type(iu))
# print(type(jimin))
# print(type([1,2,3]))
# print(type([]))

# # 메서드를 호출할 수 있음
# print(iu.greeting())

# # 속성을 부여할 수 있음
# iu.name = '아이유'
# jimin.name = 'BTS 지민'
# print(iu.name)
# print(jimin.name)
# print(type(iu.name)) # <class 'str'>
# print(type(jimin.name)) # <class 'str'>



# class Person:

#     # 생성자 메서드
#     def __init__(self, name):
#         self.name = name
    
#     def greeting(self):
#         return f'안녕...난 {self.name}'

# # 인스턴스 생성
# p1 = Person('안드레 아이유')
# print(p1.greeting()) # 직접 greeting을 호출!

# p2 = Person('뉴진스') # __init__메서드가 호출됨!
# print(p2.greeting()) # print(Person.greeting(p2))

# # Person('아이유')
# # 파이썬 내부적으로 함수를 실행
# # Person.__init__(xxxx, '아이유')



# 소개팅
# 사람 관련 정보 뭐가 있을까요?

class Person:


    def __init__(self, name, age, mbti):
        self.name = name
        self.age = age
        self.mbti = mbti
    
    def greeting(self):
        return f'{self.name}입니다. {self.mbti}이구요...'

    def __gt__(self, other):
        if self.age > other.age:
            return self
        else:
            return other
    
    def __str__(self):
        return f'{self.name} ({self.age})'



p1 = Person('재용', 30, 'istp')
p2 = Person('유영', 28, 'enfj')
print(p1.name)
print(p1.greeting())
print(p1 > p2)
print(p1)