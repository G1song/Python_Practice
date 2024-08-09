# --------------------------------------------
# 1. 함수의 다양한 입력들 살펴보기 
#
# 1) input이 없는 함수 
# 2) input이 여러 개 있는 함수 
# 3) input이 정해지지 않은 갯수만큼 있는 함수 
# --------------------------------------------

def pi():
    """원주율을 소숫점 두 자리까지 반환하는 함수
    """


    pi_value = 3.141592653589793
    return round(pi_value, 2)

#round(a, b) : a를 소수점 둘째자리까지 반올림하는 메서드 


def left_append(lst, elem):
    """lst의 왼쪽에 elem을 넣고, lst를 반환하는 함수 
    """

    lst.insert(0, elem)
    return lst 

    fruits = ['apple', 'banana', 'grapes', 'melon']
    result = left_append(fruits, 'lemon')
    print(fruits)



# 함수 호출 및 출력 예제
# my_list = [2, 3, 4]
# result = left_append(my_list, 1)
# print(result)  # [1, 2, 3, 4]

def left_extend(lst, *elem):
    """lst의 왼쪽에 정해지지 않은 갯수의 elem을 넣고 lst를 반환하는 함수 
    """
    lst[0:0] = elem
    return lst 

#함수 호출 및 출력 예제
# result = left_extend(fruits, 1,2,3)
# print(result) 


# --------------------------------------------
# 2. 함수의 call stack 알아보기 
# 
# 1) 아래 함수 b()를 실행할 때, 실행된 함수의 순서는?
# --------------------------------------------

def a():
    return pi()

def b():
    return a()

# 순서: b() ->  a() ->  pi()

# --------------------------------------------
# 2) 아래 함수 c()를 실행할 때, 실행된 함수의 순서와 각 함수의 input은? 
# --------------------------------------------

def c(lst):
    print(lst[0])

    return c(lst[1:]) 

c(list(range(10)))


