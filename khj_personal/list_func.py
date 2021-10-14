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

# insert(idx,val) 로 idx 자리뒤에 val 값 추가

a = [1, 2, 3, 4, 5, 6, 7]
print(a.pop()) # 맨뒤(오른쪽) pop
print(a.pop(2)) # idx [2] 값 pop
print("----------------------------------")

# pop(idx) 로 idx번째 값 out

a = [1,2,3]
a.remove(2)
print(a)
print("----------------------------------")

# remove(val) 로 val 값 없애기

print(a.index(3))

# index(val) 로 val의 idx(위치) 값 받음
# *
# 없는 값을 index 로 찾으려고 하면 [ERROR] 남
# *

a = [1,5,3,2,6,8,7,9]

a.sort()
print(a)

a.sort(reverse=True)
print(a)

# sort() 로 오름차순 정렬
# sort(reverse=True) 로 내림차순 정렬



