'''
01. 클래스 

클래스: 제품의 설계도
객체: 클래스로 만든 제품
속성: 클래스안의 변수
메서드 : 클래스 안의 함수
생성자: 객체를 만들 때 실행되는 함수
인스턴스 : 메모리에 살아있는 객체 (그냥 객체라고 생각하셈)


'''

class Monster:
    def say(self):
        print("나는 몬스터다") 

'''
객체 = 클래스이름() '요 클래스로 객체를 만든다' 만들었으면 객체가 생성됐겠지! 
객체.메서드()       그 객체의 메서드() 

'''

shark = Monster()
shark.say() 

class Monster:
    def __init__(self, name):
        self.name = name  #'Monster함수에 name 속성을 할당하겠다!'
    def say(self):
        print(f"나는 {self.name}")

shark = Monster("상어") #몬스터 클래스로부터 shark 라는 객체를 만드는데 매개변수로
#상어를 넣어주겠다
#가장먼저 생성자가 호출됨

shark = Monster("상어") #"상어" 가 name 자리, self는?? 객체 자기자신!!!!! shark 잡채 
#즉 shark 객체의 name 속성을 상어로 하겠다. 
shark.say() #shark 의 say 메서드를 호출하겠다 -> 나는 shark.name(즉, "상어")

wolf = Monster("늑대") 
wolf.say() #나는 self.name = 나는 늑대 

class Monster:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say(self):
        print(f"나는 {self.name}, {self.age}살임")

shark = Monster('상어', 7)
wolf = Monster('늑대' ,200)

shark.say()
wolf.say()

values = []
for x in range(10):
    values.append(x)
#list comprehension
values = [x+1 for x in range(10)]
print(values)
# 변수 = [왼쪽에답넣을 값 for i in range()]

#0-50까지 짝수 
even = [i for i in range(51) if i % 2 == 0]
print(even)

options = ['any', 'albany', 'apple', 'world', 'hello', '']
valid_strings = [strings for strings in options 
                 if len(strings) >= 2
                 if strings[0] == 'a' 
                 if strings[-1]== 'y']
print(valid_strings)


#Flattening a matrix (list of lists)
matrix = [[1,2,3], [4,5,6], [7,8,9]]
flattend = []
for row in matrix:
    for num in row: 
        flattend.append(num)

flattened = [num for num in row for num in row]
print(flattened)

#categorize numbers as even or odd
categories = []
for number in range(10):
    if number % 2 == 0:
        categories.append("even")
    else:
        categories.append("odd")
print(categories)

categories = ["even" if number % 2 == 0 else 'odd' 
              for number in range(10)]
print('answer :', categories)

#3d list = So i want a list inside of a list, inside of another list
import pprint
printer = pprint.PrettyPrinter()

lst = []
for a in range(5):
    l1 = []
    for b in range(5):
        l2 = []
        for num in range(5):
            l2.append(num)
        l1.append(l2)

    lst.append(l1)

lst = [[[num for num in range(5)] for _ in range(5)] for _ in range(5)]
printer.pprint(lst)

#list comp with functions
def square(x):
    return x**2

squared_numbers = [square(x) for x in range(10)]
print(squared_numbers)

#creating a dictionary comp
pairs = [('a', 1), ('b',2), ('c', 3)]

my_dict = {k: v for k, v in pairs}
print(my_dict)

#removing duplicates from a list while applying a function
nums = [1,2,2,3,3,3,4,4,4,4]
unique_squares = {x**2 for x in nums}
print(unique_squares) #별도의 문법을 쓰지않고 {set,set} 집합쓰면 자동 중복제거. 


#Generator comprehension 생성자 generator 다시 보기 
sum_of_squares = sum(x**2 for x in range(1000000))
print(sum_of_squares)

my_list = [1,2,3,4,5]
new_list = my_list[1:-2] 
print(new_list)

print(max(my_list), my_list.index(max(my_list)))
#최대값 찾기: max(), 최대값 인덱스찾기: self.index(max(self))

#트리 코드 구현
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
#루트를 찾는 search 함수 구현
    def search(root, value):
        if root is not None:
            if root.value == value:
                return True
            if search(root.left, value):
                return True
            if search(root.right, value):
                return True 
my_list = [9,8,7,6,5]
def solution(my_list):
    answer = []
    for i in my_list:
        if i > 7:
            answer.append(i)
    return answer
print(solution(my_list))
