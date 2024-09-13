import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

fpath = './dataset'


#csv file read
frame = 'cars.csv'
file = os.path.join(fpath, frame)
#print(file)

cars_df = pd.read_csv(file, header = 0, sep =',')
# print(cars_df.head(10))
#print(file)


fish_df = pd.read_csv("https://bit.ly/fish_csv")
fish_df.head()


#Dataframe 속성, 메서드
excel_name = 'mtcars.xlsx'
mtcars_df = pd.read_excel(os.path.join(fpath, excel_name))


# print(type(mtcars_df))


##
# print(mtcars_df.head())
# print(mtcars_df.tail())
# print(mtcars_df.info())

##
# print("index = \n", mtcars_df.index)
# print("shape = \n", mtcars_df.shape)
# print("dtypes = \n", mtcars_df.dtypes)
# print("columns = \n", mtcars_df.columns)

##데이터한눈에 보기
# print(mtcars_df.describe())
mtcars_df["cyl"] = mtcars_df["cyl"].astype("category")
mtcars_df["am"] = mtcars_df["am"].astype("category")
mtcars_df["vs"] = mtcars_df["vs"].astype("category")
# print(mtcars_df.describe())



# print(mtcars_df.head())
# print(mtcars_df.info())

##DataFrame ## 데이터만들기
data = {
    "name":["홍길동", "임꺽정", "이순신"],
    "algor":["A", "B", "C"],
    "basic":["C", "B", "B+"],
    "python": ["B+", "C", "C+"]
}

# print(data)
mydf = pd.DataFrame(data)
# print(mydf)

##
school_list = [[15, "남", "덕영중"],
               [17, "여", "수리중"]]
# print("school list = \n", school_list)
school_df = pd.DataFrame(school_list, 
                         columns = ["나이", "성별", "학교"])
# print(school_df)

# print("*"*100)
# print(school_df.index)
# print(school_df.columns)


##요약통계량 (summary statistic)
print(sns.get_dataset_names())
mpg_df = sns.load_dataset("mpg")
print(mpg_df.head())
print("shape = ", mpg_df.shape)
print("info = \n", mpg_df.info())
print("변수명 = \n", mpg_df.columns)

#실습
exam = [[90, 98, "남", True],
        [80, 89, "남", False],
        [70, 95, "여", True]
        ]
print("exam_df = \n", exam)
exam_df = pd.DataFrame(exam, 
                         columns = ["수학", "영어", "성별", "합격"])
#print(exam_df)

print('*'*50)

#exam요약통계량 #ndim = number of dimension
# print("shape = ", exam_df.shape)
# print("column names = ", exam_df.columns)
# print("ndim = ", exam_df.ndim)
# print("dtype = \n", exam_df.dtypes)


## 연속형 자료 
# print("head = \n", mpg_df.head())
print(mpg_df["mpg"].mean(skipna = True).round(3))
print(mpg_df["mpg"].median())
print(mpg_df["mpg"].var().round(3))
print(mpg_df["mpg"].std().round(3))
print(mpg_df["mpg"].sem().round(3))
print(mpg_df["mpg"].max())
print(mpg_df["mpg"].min())

##이산형자료
print(mpg_df["cylinders"].value_counts())
print(mpg_df["origin"].value_counts())
print(mpg_df[["mpg", "weight"]].mean(axis = 1).round(3))
print(mpg_df[["mpg", "weight"]].mean(axis = 0).round(3))

print('quantile = 0.25')
print(mpg_df[["mpg", "weight"]].quantile(0.25))

## correlation - 둘이 얼마나 상관이 있냐 
print("correalation coefficient(상관계수) = \n")
print(mpg_df[["mpg", "weight"]].corr())

plt.scatter(mpg_df["weight"], mpg_df["mpg"]) #반드시 x축에원인변수. y는결과변수
# weight , mpg 자리 바뀌면 안됨. 무게가 원인변수고 연비는 결과니까. 
plt.title("Weight vs MPG")
plt.xlabel("Weight (kg)")
plt.ylabel("MPG (mile/gallon)")
# plt.show()

##타이타닉 실습 - 하이클래스가 더 많이 살았을까? 남자가 정말 많이 죽엇나?
# 1. 타이타닉 데이터셋 가져오기 (seabornlibrary 에 있음)
titanic = sns.load_dataset('titanic')
print("titanic HEAD = \n", titanic.head())

# print(titanic.describe()) #2. 데이터셋의 수치정보 가져오기 describe
print(titanic.dropna().describe()) 
# 이렇게 dropna() 사용시 null 값 제거. 제거 전의 data 개수와비교
print('*'*50)

#3. 도대체 클래스별로 몇 명이 탔지?
print("groupby class = \n", titanic.groupby('class').count())
sns.countplot(y='class', data=titanic)

print("survived = \n", titanic['survived'].value_counts(), "\n")
print('*'*50)
print("mean = \n", titanic[["age", "fare"]].mean().round(3), "\n")
print('*'*50)
print("std = \n", titanic[["age", "fare"]].std().round(3), "\n")



#Q1. 데이터셋 잘라진거말고 전체 보고싶을경우? 