from random import randint 

def random_player(x_or_o, x_positions, o_positions):
    move = (0, 0)
    while move in x_positions + o_positions: #중복된 위치처리. 이미 다른 플레이어에 의해 선택된 위치인지 확인 
        x = randint(0, 2)  #(0,0)~(2,2) 사이의 임의의 위치 선택
        y = randint(0, 2)
        move = (x, y) #move 에 선택된 위치를 저장하고 이를 반환. 위치는 (x,y)형태의 튜플형태로 반환 
    return move 


x_positions = [(x, y)]
x = randint(0,2)
y = randint(0,2)

o_positions = []



if x_or_o = 'X'

x_positions  = (x,y)
if y == 0 :
    x = randint(0,2) 
elif y == 1 :
    x = randint(0,2) 
else: #y == 2: 
    x = randint(0,2)
    


def smart_player(x_or_o, x_positions, o_positons):
    return random_player(x_or_o, x_positions, o_poistions)

    #PLAY 함수 짜기 