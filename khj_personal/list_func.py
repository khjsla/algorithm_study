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
print("----------------------------------")

# sort() 로 오름차순 정렬
# sort(reverse=True) 로 내림차순 정렬

a = [1,2,3,4,5,6,7]
print(a[:3])
print(a[1:3])
print("----------------------------------")

#[idx: idx] 첫 idx 부터, 뒤 idx 앞까지 출력

print(len(a))
print("----------------------------------")

# len() 으로 길이 구할 수 있음

for x in enumerate(a):
    print(x)
print("----------------------------------")

# enumerate: tuple 형태로 출력시킴!
# (idx, val) 값이 순서대로 출력!

# * tuple = list 와 비슷하나. 값을 변경 못한다는 특징이 있음! 

for x in enumerate(a):
    print(x[0], x[1])
print("----------------------------------")

for idx, val in enumerate(a):
    print(idx)
    print(val)
print("----------------------------------")

# 자주 사용되는 enumerate 형태!

if all(5 > x for x in a):
    print("yes, all small than 60")
else:
    print("no, not all small than 60")
print("----------------------------------")

# all(5 > x for x in a) 왼쪽의 표현식을 잘 기억해둬라!