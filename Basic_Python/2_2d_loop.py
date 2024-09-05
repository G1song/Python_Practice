#학습내용: 이중 for문 

# y는 0부터 9까지 증가한다.

for y in range(0, 10):
    # x는 0-9까지 증가한다.
    for x in range(0, 10):
        # y와 x를 동시에 출력, 값의 변화를 관찰
        print(f"y = {y}, x = {x}")
        