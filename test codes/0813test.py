# # fruits = ['사과', '딸기', '포도', '체리']
# # fruits.insert(1,'바나나')
# # print(fruits)

# # score_list = [90, 98, 80, 97, 59, 30]
# # number = 1
# # for score in score_list:
# #     if score >= 60:
# #         result = "합격"
# #     else:
# #         result = "불합격"
# #     print("{}번 학생은 {}입니다.".format(number, result))
# #     number += 1

# #97부터 77까지 출력
# # for i in range(97,76,-1): #i is short for index    
# #     print(i, end=' ')


# # #23부터 40까지 출력
# # for i in range(23, 41):
# #     print(i, end=' ')
# # print()

# # list1 = [[1,2], [3,4], [5,6]]
# # for i, j in list1:
# #     print(i)
# #     print(j)       


# # #while문
# # number = 1
# # while number <=3:
# #     print(number)
# #     number += 1


# # #while문을 사용하여 "파이썬최고"를 12번 출력하시오.
# # number = 1
# # while number <= 12:
# #     print("{}번째: 파이썬최고".format(number))
# #     number += 1

# # while True:
# #     print("뫼비우스의 띠")
# #     break

# # #두개의 정수를 입력받아 더하는 코드를 작성. (단 두개의 정수가 0이 들어올때까지반복)
# # while True:
# #     num1 = int(input("첫번째정수: "))
# #     num2 = int(input("두번째정수: "))
    
# #     if num1 == 0 and num2 == 0:
# #         break

# #     print("두 수의 합은: {}".format(num1 + num2))
# # print("프로그램이 종료되었습니다.")

# # #랜덤으로 1부터 45사이의 숫자를 뽑으면 뽑은 숫자를 맞추는 up,down 게임 예제
# # import random
# # number = random.randint(1, 45)


# # while True: 
# #     num1 = int(input("숫자를 입력하세요: "))
# #     if num1 > number:
# #         print("{}보다 작은 수 입니다.".format(num1))
# #     elif num1 < number:
# #         print("{}보다 큰 수 입니다.".format(num1))
# #     else:
# #         print("정답을 맞추셨습니다 짝짝짝!!")
# #         break

# #두개의 정수를 입력받아 첫번째 정수부터 두 번째 정수까지 출력되는 코드
# num1 = int(input("첫번째 정수 입력해: "))
# num2 = int(input("두번째 정수 입력햇: "))
    

# if num1 < num2:
#     for i in range(num1, num2 +1 , 1):
#         print(i, end= ' ')
# elif num1 > num2:
#     for i in range(num1, num2-1, -1):
#         print(i, end= ' ')
# else:
#     print(num1)

#1부터 100사이의 숫자 중 3의 배수인 값들의 합을 출력
total_sum = 0 #합계를 저장하는 변수 일단 출력하고 싶은 그 값을 담을 변수를 정해. 
for i in range(1, 101):
    if i % 3 == 0:
        total_sum += i  #값 누적시 사용 
print(total_sum)

#함수
# list 에서 최대값을 구하는 함수  
lst = [5,98,5,6,8,5,41,2,6,9,8,7,69,3,6]

def my_max(lst, cmp = lambda x, y: x if x > y else y):
    max_value = lst[0]
    for i in lst[1:]:
        max_value = cmp(max_value, i)
    return max_value #for 랑 단을 맞춰야 for 문을 다~ 돌고 난 최종값이 리턴됨. 
print(my_max(lst))

# list 에서 최소값을 구하는 함수 
def my_min(lst, cmp = lambda x, y: x if x<y else y):
    min_value = lst[0]
    for i in lst[1:]:
        min_value = cmp(min_value, i)
        return min_value   #첫번째 비교가 이루어진 후에 리턴이 되어벌임;; 
print(my_min(lst))         #리턴은 루프 밖에 있어야 루프가 끝난 후 최종값이 반환됨. 






    
        

    
