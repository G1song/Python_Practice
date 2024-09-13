import os

# os.getcwd : getcurrentworkingdirectory 현재의 디렉토리 
# os.chdir : change directory 
# os.listdir : 해당 경로에(데스크탑) 어떤 파일과 폴더가 있는지 보기
# os.rename('test1.py, 'demo1.py) 


print(os.getcwd()) 
os.chdir('C:\\Users\\user\\Desktop\\')

os.rename('test1.py', 'demo1.py') 

# os.mkdir('Jiwon_Demo\\sub-dir-1')
# os.makedirs('Jiwon_Demo\\sub-dir-1')


print(os.listdir())


