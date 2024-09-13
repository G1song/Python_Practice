"""Implement a better finder to find the right argument for the function. 

Your job is to implement a function that accepts another function(call this f) and additional information(related to possible candidates) as input, and returns the argument that f returns True. 

As a hint, f will return 'up' or 'down'. When f needs larger input value to return True, it will return 'up'. Else, it will return 'down'. 

You will be asked to implement 2 finder functions; naive_finder and smart_finder. 

1) naive_finder

Function naive_finder assumes that the test function only accepts integer inputs; therefore, naive_finder can (naively) iterate all the possible candidates. It will take long - but that's why it's called naive.  Function naive_finder accepts another function f and a candidate list as input. When naive_finder is called, it iterates over all possible candidates, applies all candidates to the function one at a time, and returns when the result is True. 

naive_finder should be able to find right argument for updown_game.updown_game_easy and updown_game.updown_game_medium. 

2) smart_finder

Function smart_finder accepts another function, and the max/min value of the input for the function f. To implement the smart_finder function, think of how you actually play '업다운 게임'. 

smart_finder should be able to find right argument for updown.game.updown_game_hard and animation.check_collision. 
"""

def manual_finder(f):
    while True:
        i = input(f'Guess the argument!\nGuess is: ')
        res = f(float(i))
        if res is True:
            print(f'You found the right argument!; {float(i)}')
            return float(i)
            
        print(res) 
 
def naive_finder(f, lst):
    
    for i in lst :
        #정해진 답 == 컴터가 찍은 답이 == true
        if f(i) == True :
            return  i



def smart_finder(f, min_input = 0, max_input = 100):
    
    answer = (min_input + max_input) / 2 
     
    while True: # 이 함수가 호출되면 평생 반복해 (while 뒤의 조건식이 참일 때까지 계속 반복해)
        res = f(float(answer))
        print(answer)
        if res == 'up' :
            answer = answer + answer / 2
            res = f(float(answer))
        elif res == 'down' :
            answer = answer - answer / 2
            res = f(float(answer))
        
        if res is True:
                print(f'You found the right argument!; {float(answer)}')
                return float(answer)
              
    
    #f함수는 인자 하나를 받아서 True 또는 False 를 반환하는 함수. or return up /down 
    #naive_finder 함수 구현 방법: 
    #lst 에 있는 각 후보들을 하나씩 f함수에 넣어서 결과를 확인. 
    #f함수의 결과가 True를 반환할 때까지 모든 후보를 확인. 
    #따라서 naive_finder 는 단순히 후보 리스트를 순회하며 첫 번째로 True를 반환하는 인자를 찾는 방식 
    #lst 에 있는 각 후보들을 순회하며 (for문 사용) f(candidate)함수 호출. 
    #결과가 True 이면 해당 후보를 반환하고 함수 종료  
    