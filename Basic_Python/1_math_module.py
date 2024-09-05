# # math_module.py - 사칙연산 함수를 모은 파일

# def add(x,y):
#     result = x + y
#     return result


# def sub(x,y):
#     result = x - y 
#     return result 


# # from 모듈명 import  함수명 - 특정 모듈에서 특정 함수만 불러오는 방법
# # import 와의 차이점: import 는 특정 모듈의 모든 함수 불러옴

# # math_module 에서 add 함수만 불러오는 코드 
# # from math_module import add 

# #import 를 통해 불러온 함수는 모듈명없이 바로 호출 가능. 
# import math
# result = add(10, 1)
# print(f"result = {result}") 

# # 파이썬 내장 모듈
# # random, time 

import random 

#난수를 다루는 모듈 

#0 ~ 10 사이 (10을 포함한) 정수 중 하나를 돌려준다. 
random_number = random.randint(0,10)
print(random_number)

#리스트 중 하나의 원소를 랜덤으로 선택해서 돌려준다. 
random_choice = random.choice([1,2,3,4,5])
print(random_choice)

import time

# 시간(초)와 관련된 모듈
# 일정 시간(초) 프로그램의 실행을 중지하는 함수
# time.sleep(초)



#사용자에게 시간을 입력받는 타이머
N = int(input("타이머 시간을 입력하세요 : "))

print(f"{N}초 타이머 시작")

for t in range(N):
    print(f"{t}초가 지나갔습니다.")
    time.sleep(1)

print("타이머종료")

#현재 시간을 초로 만들어서 돌려준다. 
#1960.01.01 0시0초부터 현재까지의 차이를 초로 변환한 숫자를 돌려준다 
second = time.time()

print(second)

#프로그램의 실행 시간 측정
start = time.time() #프로그램의 실행 시간

mylist = []

for _ in range(1000000):
    mylist.append(1)

end = time.time() #프로그램의 종료시간
print(end - start) 
