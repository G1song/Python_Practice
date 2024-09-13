

# a = {1:2, 3:4, 4:5}
# print(a[1])
# print(a[3] + a[4])
# a[5] = 3

# for k, v in a.items():
#     print(k,v)


# def hello(hello_to):
#     return 'hello ' + hello_to

# hello('world')
# print(hello('world'))

all_smallcase_letters = 'abcdefghjklmnopqrstuwxyz'
#ns: {'all_smallcase_letters' : 'abcdefghjklmnopqrstuwxyz'}

upper_to_lower = {} 
lower_to_upper = {}
#ns: {'all_smallcase_letters' : 'abcdefghjklmnopqrstuwxyz', 'upper_to_lower' = {}}

for c in all_smallcase_letters:
   upper_to_lower[c.upper()] = c
   lower_to_upper[c] = c.upper()
#ns: {'all_smallcase_letters' : 'abcdefghjklmnopqrstuwxyz', 'upper_to_lower' = {}, 'A':'a', 'B':'b'...'Z':'z'}
#ns에 lower_to_upper 가 없으므로 에러남. 아래를 진행하기 위해 lower_to_upper 가 있다고 가정하면 

#ns: {'all_smallcase_letters' : 'abcdefghjklmnopqrstuwxyz', 'upper_to_lower' = {}, 
#'A':'a', 'B':'b'...'Z':'z', 'a':'A', 'b':'B', 'c':'C'......'z':'Z'}


a= 'abcdf123SAFDSDF'
ans_1 = ''
ans_2 = ''
#ns: {'all_smallcase_letters' : 'abcdefghjklmnopqrstuwxyz', 'upper_to_lower' = {}, 
#'A':'a', 'B':'b'...'Z':'z', 'a':'A', 'b':'B', 'c':'C'......'z':'Z', 'a':'abcdf123SAFDSDF',
#'ans_1:'', 'ans_2:''}

for c in a :
    if c in upper_to_lower:
        ans_1 += upper_to_lower[c]
        ans_2 += c
    elif c in lower_to_upper:
        ans_1 += c
        ans_2 += lower_to_upper[c]
    else:
        ans_1 += c
        ans_2 += c

#for 문에서 c를 a에서 돌면 첫번째 c는 a가 되는데 upper_to_lower 딕셔너리는 알파벳대문자를 key 값으로 받잖음? 
#따라서 'a' 가 key 인 값은 없음. 따라서 if c in upper_to_lower:는 false 가 되고 else 로 넘어감. 
#자 그럼 else: 로 넘어와서 ans_1 += c를 하면 첫번째 c는 'a'이므로 ans_1 = 'a' 가 되고 
#저 위의 문자열 a에서 쭉 abcdf123까지 돌면서 ans_1 = 'a', ans_2 = 'A' 가 됨
#즉 KEY 값이 대문자 알파벳이 되기 전까지 ELSE 만 실행이 되는데 중간에 숫자 1이 나오면서 ERROR 발생. 
#숫자가 키값에 없으니까. 







#ans_2 += lower_to_upper[c]도 실행이 되어야 하니까 ans_2 



#이제 대문자 S차례가 오면 ns는 
#다시 if 가 true 가 되면서 ans_1 += upper_to_lower[c] 가 실행됨. 
#즉 ans_1 = abcdf123 + S:s 가 됨 즉 np에 'S':'s'가 추가됨
#ans_2 += c -> ans_2 = S 