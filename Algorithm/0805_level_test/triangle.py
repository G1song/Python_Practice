height = int(input('피라미드의 높이를 입력하세요: '))

for i in range(height):
    spaces = height - i -1 
    starts = 2*i + 1
    print(' '*spaces + '*' * starts)
    