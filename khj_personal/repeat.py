# -*- coding: utf-8 -*-
# 위 코드: 한글 python 에서 돌리는 법

# 반복문
# range() 의 세번쨰 인자
# for - else 문 
# 기억하기

for i in range(11):
    print(i)
print("----------------------------------")
for i in range(1, 11):
    print(i)
print("----------------------------------")
for i in range(5, 11):
    print(i)
print("----------------------------------")
for i in range(1, 11, 2):
    print(i)
print("----------------------------------")
for i in range(1, 11, -2):
    print(i)
print("----------------------------------")
for i in range(1, 21, 10):
    print(i)
print("----------------------------------")

# 결론 --------------------
x1 = 0  # 처음 시작 숫자
x2 = 11  # 여기서 -1 한 숫자까지 반복
x3 = 2  # 등차 값
for i in range(x1, x2, x3):
    print(i)
# ------------------------
print("----------------------------------")

for i in range(1, 11):
    if i % 2 == 0:
        break  # 그냥 for 문 끝
    print(i)
print("----------------------------------")

for i in range(1, 11):
    if i % 2 == 0:
        continue  # 아래 부분만 끝. for문 끝 아님
    print(i)
print("----------------------------------")

for i in range(1, 11):
    print(i)
    if i == 5:
        break  # 그냥 여기서 끝
else:
    print(11)
print("----------------------------------")

for i in range(1, 11):
    print(i)
    if i == 5:
        continue
else:  # for 문이 정상적으로 끝나면, else 부분이 실행됨
    print(11)
    print("checkthis !")
print("----------------------------------")

for i in range(1, 11):
    print(i)
else:  # for 문이 정상적으로 끝나면, else 부분이 실행됨
    print(11)
print("----------------------------------")
