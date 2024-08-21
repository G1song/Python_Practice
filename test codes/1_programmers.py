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
