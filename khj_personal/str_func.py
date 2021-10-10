# -*- coding: utf-8 -*-
# 위 코드: 한글 python 에서 돌리는 법

# 문자열과 내장함수

msg = "Hi khj"

print(msg.upper())
print(msg)
print("----------------------------------")

msg_cp = msg.upper()
print(msg_cp)
print("----------------------------------")

print(msg.lower())
print(msg)
print("----------------------------------")

# .lower() .upper() 로 소문자, 대문자 만들 수 있음. 
# 대신 원본은 그대로임

msg = "khjkk"
print(msg.find("k"))
print("----------------------------------")

# .find("?") 로 ? 의 위치 idx 값 얻을 수 있음
# but 가장 처음의 것이 return 됨

msg = "khjkk"
print(msg.count("k"))
print("----------------------------------")

# .count("?") 로 ? 개수 구할 수 있음

msg = "abcdefg"
print(msg[:2]) #0~1 까지만 추출
print("----------------------------------")

msg = "abcdefg"
print(msg[3:5]) #0~1 까지만 추출
print("----------------------------------")

# [x:y] 로 문자열 slice 가능

for x in msg:
    print(x)
print("----------------------------------")

# for x in ?: 로 글자 "?" 를 하나 하나 catch 가능

msg = "abcDEF"
for x in msg:
    if x.isupper():
        print("THIS IS BIG", x)
    if x.islower():
        print("THIS IS SMALL", x)
print("----------------------------------")

# isupper(), islower()를 통해 대/소문자 구분 가능

msg = "AZ"
for x in msg:
    print("CHAR to ASCII", ord(x))
print("----------------------------------")

msg = "az"
for x in msg:
    print("CHAR to ASCII", ord(x))
print("----------------------------------")

# ord() 를 통해 문자의 ASCII(숫자)값 알 수 있음
# A = 65
# Z = 90
# a = 97
# z = 122

msg = 65
print("ASCII to CHAR", chr(msg))
print("----------------------------------")

# chr() 를 통해 숫자(ASCII)의 문자값 알 수 있음