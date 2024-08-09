all_smallcase_letters = 'abcdefghijklmnopqrstuvwxyz'

# --------------------------------------------
# 1. list/tuple 기초 예제들 
# 
# a는 1,2,3이 들어간 튜플, 
# b는 a부터 z까지 모든 알파벳 소문자가 들어간 리스트가 되도록 만들어보세요. 
# b를 만들 때 위에 주어진 all_smallcase_letters와 for loop를 사용해도 좋고, 손으로 다 쳐도 좋습니다. 
# --------------------------------------------

# write your code here 

a = (1,2,3)

#b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
b = []
for i in all_smallcase_letters:
    b.append(i)
print(b)

# --------------------------------------------
# 2. dict 기초 예제 
# 
# 1) upper_to_lower
#
# upper_to_lower은 모든 대문자 알파벳(ex. A)을 key로 가지고, 대응하는 소문자 알파벳(ex. a)을 value로 가지는 dict입니다. 
# 위에서 만든 b와 for loop를 이용해서 upper_to_lower을 만들어보세요. 
# 
upper_to_lower = {}
for i in b:
    upper_to_lower[i.upper()] = i 
print(upper_to_lower) #return 으로 하면 안되나? 안되는 이유는?  
#return 은 함수안에서만 사용가능 




# 2) lower_to_upper
## upper_to_lower과 반대로 된 dict를 만들어보세요. 

lower_to_upper = {}
for i in b:
    lower_to_upper[i] = i.upper()
print(lower_to_upper)

# 
# 3) alpha_to_number
# 
# 소문자 알파벳 각각을 key, 몇 번째 알파벳인지를 value로 가지는 dict를 만들어보세요. 
# 위 all_smallcase_letters와 enumerate함수를 사용하세요. 
# 알파벳 순서는 1부터 시작합니다. ex) alpha_to_number['a'] = 1

alpha_to_number = {}

for idx, i in enumerate(b, start = 1) :
    print(idx, i)
    alpha_to_number[i] = idx
print(alpha_to_number)


# my_dict = {}
# for i in enumerate(b, start = 1):
#     print(i)
#     my_dict[i[1]] = i[0]
# print(my_dict)


# 4) number_to_alphabet 

# 1부터 26까지의 수를 key로, 소문자, 대문자로 이뤄진 문자열 2개의 튜플을 value로 가지는 dict를 만들어보세요. 
number_to_alphabet = {}

for i in range(1, 27):
    letter = b[i-1] # 0-based index
    number_to_alphabet[i] = (letter, letter.upper())

print(number_to_alphabet)


# --------------------------------------------
# 3. 주어진 문자열의 대소문자 바꾸기 
#
# 위 2에서 만든 dict들을 이용하여, 아래 문제들을 풀어보세요. 
#  
# 1) 주어진 문자열을 모두 대문자로 바꾼 문자열을 만들어보세요. 
# 2) 주어진 문자열을 모두 소문자로 바꾼 문자열을 만들어보세요. 
# 3) 주어진 문자열에서 대문자는 모두 소문자로, 소문자는 모두 대문자로 바꾼 문자열을 만들어보세요. 
# 4) 주어진 문자열이 모두 알파벳이면 True, 아니면 False를 출력하는 코드를 짜보세요. 
# --------------------------------------------

a = 'absdf123SAFDSDF'

#1) 문자열 모두 대문자로 
a_list = list(a) #문자열을 문자 리스트로 변환 
upper_a = ''     #결과를 저장할 빈 문자열 

for i in a_list:
    upper_a += i.upper()

print(upper_a) 

for i in a_list:
    if i in lower_to_upper:
        upper_a += lower_to_upper[i]
    else:
        upper_a += i

# for i in a_list:
#     if i.islower(): #문자가 소문자인 경우 islower() if i.islower():
#         upper_a += i.upper() 
#     else:
#         upper_a += i #대문자가 아닌 경우 그대로 추가 

# print(upper_a)  


# 2) 문자열 모두 소문자로 
a_list = list(a)
lower_a = ''

print('upper_to_lower', upper_to_lower)
for i in a_list:
    if i in upper_to_lower:
        lower_a += upper_to_lower[i]
    else:
        lower_a += i 

print(lower_a)


# 3) 대문자는 소문자로, 소문자는 대문자로 
switch_a = ''

# print(switch_a)


# 4) 주어진 문자열이 모두 알파벳이면 True, 아니면 False를 출력

# if a.isalpha():    #isalpha(): 주어진 문자열이 '모두' 문자열인지 확인하는 함수
#     print("True")
# else:
#     print("False") 

a = 'sfsdafsfsfd1'
all_smallcase_letters = 'abcdefghijklmnopqrstuvwxyz'
all_uppercase_letters = all_smallcase_letters.upper()

flag = True
for i in a:
    # flag = flag and (i in all_smallcase_letters + all_uppercase_letters)
    if i in all_smallcase_letters + all_uppercase_letters:
        pass 
    else:
        flag = False 
print(flag)




# for i in string:
#     if i in all_smallcase_letters or all_upper_letters:
#         print("True")
#     else:
#         print("False")  
# print(string)







# --------------------------------------------
# 4. 다양한 패턴 찍어보기 
# 
# 1) 피라미드 찍어보기 - 1 
#
# 다음 패턴을 프린트해보세요. 
#
#     *
#    ***
#   *****
#  *******
# *********
# --------------------------------------------

# write your code here 

h = 5 
n = range(1, 6)

for i in n:
    line = ' '*(h-i) + '*' * (2*i -1)
    print(line)












# --------------------------------------------
# 2) 피라미드 찍어보기 - 2 
# 
# 다음 패턴을 프린트해보세요. 
# 
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# --------------------------------------------

# write your code here 

# --------------------------------------------
# 3) 피라미드 찍어보기 - 3 
# 
# 다음 패턴을 프린트해보세요. 
#
#     A 
#    A B 
#   A B C 
#  A B C D 
# A B C D E 
# --------------------------------------------

# write your code here 

# --------------------------------------------
# 4) 피라미드 찍어보기 - 4 
# 
# 다음 패턴을 프린트해보세요. 
# 
#       1 
#      1 1 
#     1 2 1 
#    1 3 3 1 
#   1 4 6 4 1
# --------------------------------------------

# write your code here 


# --------------------------------------------
# 5) 다음 패턴을 찍어보세요. 
# 
# *         *         * 
#   *       *       *   
#     *     *     *     
#       *   *   *       
#         * * *         
#           *           
#         * * *         
#       *   *   *       
#     *     *     *     
#   *       *       *   
# *         *         * 
# --------------------------------------------

# write your code here 


