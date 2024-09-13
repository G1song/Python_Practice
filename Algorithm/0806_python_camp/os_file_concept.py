import os 
import pickle 

# # --------------------------------------------
# # 1. os 기초 예제 
# # 
# # 1) os.path 이해하기 (os.path.exists, os.path.join, os.path)
# # 2) os.listdir / os.makedir 해보기 
# # 3) os.getcwd / os.changedir 해보기 
# # --------------------------------------------

# import os
# current_directory = os.getcwd()
# print(f'현재 작업 디렉터리: {current_directory}')

# # print(os.getcwd()) 

# for elem in os.listdir(): 
#     if os.path.isdir(elem):
#         print('<DIR>\t\t' + elem)
#     elif '.' in elem:
#         extension = elem.split('.')[-1]
#         print(f'{extension} file\t\t{elem}')

# def create_dir(directory_name):
#     if not os.path.exists(directory_name):
#         print(f'{directory_name} does not exist;')
#         os.makedirs(directory_name)

#     else: 
#         print(f'{directory_name} does exist;')

# create_dir('hello world')

# --------------------------------------------
# 2. file 기초 예제 
# 
# 1) open 이해하기 
# 2) 파일 읽기, 써보기 
# --------------------------------------------
#파일은 무조건 여는 걸로 시작하고 닫는 걸로 끝남. 

from time import time

begin = time()
f = open('example.txt', 'w+', encoding = 'utf-8') 

#example이라는 텍스트파일을 'W+' (만들어서 쓸거야), utf-8 로 인코딩할거야
# w: 사용할거야  w+: 사용할거를 만들거야   r: 읽기만  a+: append 추가할거야

for i in range(100):
    # print(i, file = f)
    #f.write(str(i) + '\n')
    print(1, file = f)

f.close()
end = time()
print(f'{end - begin} seconds')

#cmd 화면에서 한 번 실행하고나서 example.txt 파일을 봐야함. 
#f.read(): 파일을 한번에 읽어옴
#f.readline(): 파일을 한줄씩 읽어옴 
#f.readlines(): 파일을 한줄씩 끝까지 불러옴. 
# 한줄씩 불러올 때 맨 위에부터 읽는 것이 아니라 책갈피처럼 해당 부분 다음부터 읽음. 




# --------------------------------------------
# 3. pickle 기초 예제 
# 
# 1) pickle.load() 해보기 #하드에 절이듯 넣었던 피클을 꺼내쓰고싶을 때
# 2) pickle.dump() 해보기 #하드디스크에 피클절이듯 넣어두는 것
# --------------------------------------------
#'wb+' : byte 를 쓴다. rb: byte 를 읽는다. 



d = {'사과':'맛있어', '비행기':'길어', 'key':'value'}

pickle.dump(d, open('empty_dict.pickle', 'wb+'))

e = pickle.load(open('empty_dict.pickle', 'rb'))

print(e)