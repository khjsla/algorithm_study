# -*- coding: utf-8 -*-

# 시험보기전에 꼭 봐
# [ 입력 ]

"""
# 1. 기본 입력
print("1. 기본 입력")
x = input()
print(x)

# 2. 1차원 배열 입력
print("2. 1차원 배열 입력")
x_list = list(map(int, input().split()))
print(x_list)

# 3. 한 줄에 정수 여러개를 여러 변수에
print("3. 한 줄에 정수 여러개를 여러 변수에")
a, b, c, d = map(int, input().split())
print(a)
print(b)
print(c)
print(d)

# 4. 한 줄에 문자열 변수 여러개
print("4. 한 줄에 문자열 변수 여러개")
a, b = input().split()
print(a)
print(b)

"""
a = 4
# 5. 문자열 여러개 list 로 입력받기
print("5. 문자열 여러개 list 로 입력받기")
x_list = [input() for _ in range(a)]
print(x_list)

# 6. 문자열 여러개 list 로 입력받기 (문자열 하나하나 분해해서)
print("6. 숫자 여러개 list 로 입력받기 (문자열 하나하나 분해해서)")
x_list = [list(map(int, input())) for _ in range(a)]
print(x_list)

# 7. 2차원 배열의 숫자 입력받기
print("7. 2차원 배열 입력받기")
x_list = [list(map(int, input().split())) for _ in range(a)]
