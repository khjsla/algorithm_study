# Python 정리 
by. 🦔 '현지'

### [ 반복문 ]
```
range(x1,x2,x3)
# x3  = 등차
```
```
for:
else:
# for else 
# for 문 run 후, else run
```

### [ 문자열 + 내장함수 ]
```
str.lower() #소문자로 '변환'
str.upper() 

str.find("?") #? 가 있는 자리 idx 값

str.count("?") #? 몇개 있는지 

str[x:y] # x~y 까지 slice

str.islower() #소문자인지 '확인'
str.isupper()

ord(str) #문자 to ASCII(숫자)
chr(num) #숫자(ASCII) to 문자

for x in str: #문자열 순서대로 하나씩
```

### [ 리스트 + 내장함수 ]
```
a = []
b = list()

c = a+b #리스트 + 가능

a.append(val) # val 추가
a.insert(idx,val) # idx 뒤에 val 추가

a.pop() # 맨 뒤(오른) out
a.pop(idx) # idx 위치 값 out
a.remove(val) # val 값 out

a.index(val) # val의 idx 위치 값
```