all_smallcase_letters = 'abcdefghijklmnopqrstuvwxyz'

# --------------------------------------------
# 1. list/tuple 기초 예제들 
# 
# a는 1,2,3이 들어간 튜플, 
# b는 a부터 z까지 모든 알파벳 소문자가 들어간 리스트가 되도록 만들어보세요. 
# b를 만들 때 위에 주어진 all_smallcase_letters와 for loop를 사용해도 좋고, 손으로 다 쳐도 좋습니다. 
# --------------------------------------------

# write your code here 
a = (1, 2, 3)
b = []

for i in all_smallcase_letters:
    b.append(i)
print('b는','\n', b)


# --------------------------------------------
# 2. dict 기초 예제 
# 
# 1) upper_to_lower
#
# upper_to_lower은 모든 대문자 알파벳(ex. A)을 key로 가지고, 대응하는 소문자 알파벳(ex. a)을 value로 가지는 dict입니다. 
# 위에서 만든 b와 for loop를 이용해서 upper_to_lower을 만들어보세요. 

upper_to_lower = {}
for i in b :
    upper_to_lower[i.upper()] = i 
    
print('upper_to_lower는','\n', upper_to_lower)

 
# 2) lower_to_upper
#
# upper_to_lower과 반대로 된 dict를 만들어보세요. 

lower_to_upper = {}
for i in b:
    lower_to_upper[i] = i.upper()

print('lower_to_upper는','\n', lower_to_upper)

# 
# 3) alpha_to_number
# 
# 소문자 알파벳 각각을 key, 몇 번째 알파벳인지를 value로 가지는 dict를 만들어보세요. 
# 위 all_smallcase_letters와 enumerate함수를 사용하세요. 
# 알파벳 순서는 1부터 시작합니다. ex) alpha_to_number['a'] = 1

alpha_to_number = {}
for idx, i in enumerate(b, start=1):
    alpha_to_number[i] = idx 

print(alpha_to_number)


# 4) number_to_alphabet 
#
# 1부터 26까지의 수를 key로, 소문자, 대문자로 이뤄진 문자열 2개의 튜플을 value로 가지는 dict를 만들어보세요. 
# --------------------------------------------
# write your code here 


number_to_alpha = {}

for i in range(1,27):
    #key = value 부터 정의하자
    b = all_smallcase_letters[i-1]
    number_to_alpha[i] = (b.lower(), b.upper())
print('n2a', number_to_alpha)


# --------------------------------------------
# 3. 주어진 문자열의 대소문자 바꾸기 
#
# 위 2에서 만든 dict들을 이용하여, 아래 문제들을 풀어보세요. 
# --------------------------------------------

a = 'absdf123SAFDSDF'

#1) 모두 대문자로 

a_list = list(a)
upper_a = ''

# for i in a_list:
#     upper_a += i.upper() #바로 빈문자열에 리스트요소 하나씩 추가할 수 있구나 
# print(upper_a)

#.upper(), .lower() 다 쓰지말고 해봐

for i in a_list:
    if i in lower_to_upper:
        upper_a += lower_to_upper[i]
    else: 
        upper_a += i 

#2) 모두 소문자로 
a_list = list(a)
lower_a = ''

for i in a_list:
    if i in upper_to_lower:
        lower_a += upper_to_lower[i]
    else: 
        lower_a += i 


#3) 대문자는 소문자로, 소문자는 대문자로 
a_list = list(a)
switch_a = ''

for i in a_list:
    if i in upper_to_lower:
        switch_a += upper_to_lower[i]
    elif i in lower_to_upper:
        switch_a += lower_to_upper[i]
    else: 
        switch_a += i 
print('switch_a는', switch_a)

#4) 문자열이 모두 알파벳이면 True, 아니면 False를 출력

string = ''
all_smallcase_letters = 'abcdefghijklmnopqrstuvwxyz'
all_uppercase_letters = all_smallcase_letters.upper()

flag = True #기본적으로 문자열이 알파벳으로만 구성된다고 가정 

for i in string:
    if not (i in all_smallcase_letters or i in all_uppercase_letters) :
        flag = False
        break 
print(flag) 



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
    line = '  '*(h-i) + '❤️' *(2*i-1)
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

for i in n:
    line = ' '*(h-i) + '* '*i 
    print(line)

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
all_ups = all_smallcase_letters.upper()
print(all_ups)
#all_ups = ABCDEFGHIJKLMNOPQRSTUVWXYZ

print('Pyramid')
n=5

for i in range(n):
    line = ' '*(n-i-1)  
    print(line, end='')
    
    for j in range(i+1):
        print(all_ups[j], end=' ')   
    print()
    '소민님짱'
    '동준님짱'


# for i in n:
#     line = ' '*(h-i) 
#     line += '* '*i  
#     # for j in range(i):
#     #     line += '* '
#     print(line)



# all_smallcase_letters = 'abcdefghijklmnopqrstuvwxyz'
# all_ups = all_smallcase_letters.upper()

# h = 5
# n = range(1, 6)

# for i in n:
#     line2 = '  '*(h-i) + (all_uppercase_letters[0:i] + ' ')*(2*i-1)
#     print(line2)

# for i in n:
#     line3 = '  '*(h-i) + (all_uppercase_letters[i-1:i] + ' ')*(2*i-1)
#     print(line3)



#알파벳이 끝나면? 피라미드도 그냥 끝인감? 아님 다시 A부터 돌아가게도 가넝? 
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


