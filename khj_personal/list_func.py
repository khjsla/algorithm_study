# -*- coding: utf-8 -*-
# 위 코드: 한글 python 에서 돌리는 법

# 리스트와 내장함수

a = []
print(a)

b = list()
print(b)
print("----------------------------------")

#list 선언방법

a = [1,2,3]
b = ['a','b','c']
c = a+b
print(c)
print("----------------------------------")

# +로 list 이을 수 있음

a.append(4)
print(a)
print("----------------------------------")

# append() 로 뒤에 값 추가

a.insert(2,10)
print(a)
print("----------------------------------")

# insert(x,y) 로 x 자리뒤에 y 값 추가