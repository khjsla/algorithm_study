# Python ์ ๋ฆฌ 
by. ๐ฆ 'ํ์ง'

### [ ๋ฐ๋ณต๋ฌธ ]
```
range(x1,x2,x3)
# x3  = ๋ฑ์ฐจ
```
```
for:
else:
# for else 
# for ๋ฌธ run ํ, else run
```

### [ ๋ฌธ์์ด + ๋ด์ฅํจ์ ]
```
str.lower() #์๋ฌธ์๋ก '๋ณํ'
str.upper() 

str.find("?") #? ๊ฐ ์๋ ์๋ฆฌ idx ๊ฐ

str.count("?") #? ๋ช๊ฐ ์๋์ง 

str[x:y] # x~y ๊น์ง slice

str.islower() #์๋ฌธ์์ธ์ง 'ํ์ธ'
str.isupper()

ord(str) #๋ฌธ์ to ASCII(์ซ์)
chr(num) #์ซ์(ASCII) to ๋ฌธ์

for x in str: #๋ฌธ์์ด ์์๋๋ก ํ๋์ฉ
```

### [ ๋ฆฌ์คํธ + ๋ด์ฅํจ์ ]
```
a = []
b = list()

c = a+b #๋ฆฌ์คํธ + ๊ฐ๋ฅ

a.append(val) # val ์ถ๊ฐ
a.insert(idx,val) # idx ๋ค์ val ์ถ๊ฐ

a.pop() # ๋งจ ๋ค(์ค๋ฅธ) out
a.pop(idx) # idx ์์น ๊ฐ out
a.remove(val) # val ๊ฐ out

a.index(val) # val์ idx ์์น ๊ฐ
```