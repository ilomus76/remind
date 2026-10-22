# 5교시 
#1. print(), 변수 , 자료형 , input()
print("변수 만들고 데이터 출력")

# 6교시
name = "홍길동" # 문자형 데이타 (str)
age  = 25      # 수치형 - 정수 (int)
height = 175.5 # 수치형 - 실수 (float)
is_student = True # 논리값 ( bool )  - 조지불에서 따옴
print(name)
print(name, age, height, is_student) # 여러 데이타 출력 
print(f"{name}님의 나이는 { age}살 입니다.")  # format string ( f-string) 출력 

# 자료형 확인하는 파이썬의 표준기능(함수) - type()  , 자바스크립트 typeof()
print(type(name),type(age),type(height),type(is_student))


# 사용자 입력 : 키보드로 사용자 입력 데이타 받기 input() 
# user_name = input('이름을 입력하세요: ').strip() or "학생" # 양쪽 끝의 공백을 제거 , 혹시 앞의 것이 값이 없으면 학생으로 찍히게 , Enter 를 그냥 누르면 빈 값이 들어감.
# print(f"환영합니다. {user_name}님!")
print()


#2. 연산자와 문자열 유용한 기능 

a,b =10,3  # 대입 연산자는 하나를 하나에 대입 , 이 글을 튜플을 묶어서 하나씩 대입... 
print('사칙연산:', a+b, a-b, a*b,a/b)
print('몫, 나머지, 제곱:', a//b, a%b, a**b)
print('비교, 논리:', a>=b, (a>5) and (b<5))
print('비교, 논리:', a>=b, (a>5) and (b>5))

# 문자열의 여러 유용한 기능함수들 
message = "    Python Review, Python   "
print(message.strip()) # 앞뒤공백 제거,
print(message) # 원변 불변
print(message.strip().lower()) # message chaining 기술

print(message.replace('Python',"파이썬"))

print("사과,바나나,오렌지".split(',')) #응답 결과는 리스트

print('Py' in message) # message안에 Py가 있나? 
print(len(message)) # 글자수

#3. 제어문(조건, 반복)
# 점수에 따른 학점 산출

score = 82
if score >=90:
    grade = 'A'
elif score >=80:
    grade = 'B'
else :
    grade ='C'

print('학점:',grade)


# 반복문 
# for n in [1,2,3,,4,5]:  #1~5까지 반복
for n in range(1,6):
    if n == 3:
        continue
        # break  # 중간에 멈춤

    print(n)


count = 0 
while count<3:
    print(count)
    # coumt ++
    count +=1




#4. (중요) 리스트[] , 튜플 (), 딕셔너리 {key:value}, Set {} : 중복되지 않은 값들을 만들어 낼때 ( 데이타 분석의 unique), 컴프리헨션 
# 6교시 

fruits = ["사과","바나나","사과"] # 순서대로 저장, 수정 가능, 중복데이터 허용 
print(fruits)

# 리스트 : 값추가 , 삭제 가능
fruits.append('포도')
print(fruits)

fruits[1] = '오렌지'  # 특정 값 인덱스로 수정
print(fruits)


# 튜플 
point = (10,20) # 튜플 - 요소 수정 불가
print(point, point[0],point[1]) # point 와 그 요소값 출력 
#point.append() # 이런 것은 존재 안함. 튜플에서는 값 변경이 안되서 , 자동완성도 안됨
# point[0] = 100 # error 

# 딕션너리 dict 
student = {"name":"sam","score":80} # key:value pair 쌍
print(student)

student['score']=90
print(student, student['score'], student.get('name'))

# print(student['scor']) # 없어서 에러가 남 .
print(student.get('nam','없음')) # 없는 것이 오면 '없음'으로 내어 줌. 


# 중복 데이터를 허용하지 않는 Set 타입 
unique_fruits = set(fruits) # 형변화 , list를 set으로 형변환 , list(10),int(10)
print(unique_fruits) # 순서가 바뀌고 중복된것이 제거 됨 . 순서대로 나올수 있음 내부 hash로 한다고 함 , red hash로 함
# 순서는 보장 안됨. 중복 허용 안함. 


# 리스트 컴프리헨션 
#1~5의 제곱값을 저장하는 리스트 생성 , 리스트를 만드는 작업
# squares = [n**2 for n in range(1,6)] # 리스트의 값에서 하나씩 가져온 n에 대해서 n을 제곱 
squares = [n*n for n in range(1,6)] 
print(squares)

passing = [n for n in [65,90,73,82] if n>=80] # 시험 패스 조건 통과 점수들 
print(passing)

#5. 함수 , lambda
def greet(person,greeting='안녕하세요'): # person : 변수만 할당, greeting : 기본값으로 안녕하세요값 전달. 
    return f"{greeting},{person}님!"

print(greet('영희'))
print(greet('철수','반가워요'))


# 내장함수
def average(numbers):
    return sum(numbers)/len(numbers) # 총합 / 개수 = 평균 ( sum,len 내장(표준)함수)

print("평균:", average([80,90,75])) # 작성한 함수를 호출해서 실행, 리스트를 변수로 전달.

# 제곱해주는 기능 함수 --- 람다 함수로 lambda 
def square(x):
    return x*x
print(square(5))

square = lambda x:x*x
print(square(5))



#내장함수 중에서 자주 사용
print('정렬:', sorted([3,1,5,2]))
print(min(3,1,5),max(3,1,5))


# 6. 내장 함수 중에서 제일 많이 쓰는 파일 입출력 기능 함수

# 현재 파일이 있는 폴더에 결과 txt문서를 저장
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent # 기본 경로를 만들자 ...
# .resolve라고 하면 .././. 의 상대 경로를 전부 절대 경로로 대체해줌.
# C:\Users\mbc\MBCA\00 심화학습 전 리마인드 수업>01_Python>01_basic.py 가 __file__을 준다 .. 여기서 파일명을 제거 해야 함. -> parent 
# __ magic 변수 ,,, __file__ : 현재 파일의 상대 경로를 줌. 

file_path = BASE_DIR / "aaa.txt" # Path를 사용하면 /를 그냥 경로로 이해함.  윈도우에서는 \ , linux에서는 /
# file = open('aaa.txt','') # 현재 실행되는 폴더가 기준. 즉 , 실행하는 디렉토리가 다르면 실행 결과가 다름

file = open(file_path,'w', encoding="utf-8") # 없으면 파일을 만들어 냄 , 인코딩 , 
file.write('파이썬 복습 \n 파일 입출력 예제 \n')
file.close() # 메모리 위크 문제 발생을 방지하기 위해 반드시 닫아야 함. 


with open(file_path,'r',encoding='utf-8') as file: 
    # 이렇게 사용햐면 파일에 작업을 한다고 보여서 이렇게 사용
    print('파일내용:', file.read())
    # close가 자동으로 됨 왜냐하면 바로 들여쓰기가 바뀌기 때문에 ...


# 예외 처리 
number = int("80") # 문자
print(number+10) # 문자 + 숫자 는 안됨 , 형변환 해 줘야 함

# 예외 처리 (예외가 발생해도 다운되지 않도록...) 
try:
    number = int("80abc") # 문자  => 이렇게 하면 나중에 시스템이 꽝남 .. 그래서 이런 상황을 없애기 위해 에러 처리 해야 함. 
    print(number+10) # 문자 + 숫자 는 안됨 , 형변환 해 줘야 함
except ValueError as error:
    print('예외발생',error)
finally:
    print('예외여부와 상관없이 무조건 실행') # close 작업은 무조건 여기서 

# 실행
#  cd 01_Python
#  python 01_basic.py


# run 벼튼이 없어서 
# python 모듈을 설치해야 함. 