a = 'absdf123SAFDSDF'

#1) 문자열 모두 대문자로 
a_list = list(a) #문자열을 문자 리스트로 변환 
upper_a = ''     #결과를 저장할 빈 문자열 

for i in a_list:
    upper_a += i.upper()
print(upper_a)


    
