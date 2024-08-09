class MyDate: #날짜를 생성하는 클래스 

    def __init__(self, year = 0, month = 0, day = 0, hour = 0, minute = 0, sec = 0):
         #initialize :클래스가 가지고 있는 field를 초기화하는 함수
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.sec = sec
    #__init__()함수는 그냥 self.머머 = 머머 이런 식으로 쓰임. 그게 끝이니까 외워 
        
    def normalize(self): # Normalize the date and time
        if self.sec >= 60:
            self.minute += self.sec // 60
            self.sec %= 60

        if self.minute >= 60:
            self.hour += self.minute // 60
            self.minute %= 60   # self.minute 을 60분으로 나눈 나머지

        if self.hour >= 12:
            self.day += self.hour // 12
            self.hour %= 12

       

        month_31 = [1,3,5,7,8,10,12]
        month_30 = [4,6,9,11]
        month_28 = [2]
    
        if self.month in month_31:
            self.month += self.day // 31
        elif self.month in month_30:
            self.month += self.day // 30
        else:
            self.month += self.day // 28 
                       
        
        if self.month >= 12:
            self.year += self.month // 12
            self.month %= 12 

            #윤년과 윤달계산 4년 #4배수년도마다 윤년과 윤달. 
            #윤년(leap year): 하루가 더 많은 해. 366일.


        def is_leap_year(self):
            #return self.year % 4 == 0

            if self.year % 4 == 0: 
                return True   
            else:
                return False


                if 2024 % 4 == 0
                return 2024 

            
                d = MyDate(2024)
                if d.is_leap_year():
                    # ... 
                
        
                
                if month == 2:
                return 2월의 일수는 29 ㅠㅠㅠㅠㅠㅠ 
                #if self.month == 2:
                # return self.day = 29? 


                2월은 29일이라는 걸 도출하고 싶은건데 ㅠㅠㅠㅠㅠ 

                
            
        

          

    def __add__(self, other):
        new_year = self.year + year 
        new_month = self.month + month
        new_day = self.day + day
        new_hour = self.hour + hour
        new_minute = self.minute + minute
        new_sec = self.sec + sec 


    def __sub__(self, other):
        new_year = self.year - year 
        new_month = self.month - month
        new_day = self.day - day
        new_hour = self.hour - hour
        new_minute = self.minute - minute
        new_sec = self.sec - sec 

    def __eq__(self, other):
        pass 

    def __lt__(self, other):
        pass 
    
    def __le__(self, other):
        pass 

    def __gt__(self, other):
        pass 

    def __ge__(self, other):
        pass 

if __name__ == '__main__':
    d0 = MyDate()
    d1 = MyDate(2022, 4, 1, 14, 30)
    d2 = MyDate(2024, 8, 100, 23, 10) # should raise an error 
    d3 = MyDate(2024, 2, 30) # should raise an error 

    d3 = MyDate(day = 1) 
    assert d1 + d3 == MyDate(2022, 4, 2, 14, 30)
    assert d1 - d3 == MyDate(2022, 3, 31, 14, 30) 

    assert d1 < d2 


    
    
