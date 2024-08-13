import random 

# --------------------------------------------
# 1. max / min 구현하기 
#
# cmp라는 함수를 이용한 min/max 구현하기. 
# cmp는 두 원소 중 더 큰 것을 반환하는 함수. 
# --------------------------------------------

# def cmp(x,y):
#     return x if x > y, else y
#def cmp(x, y):
    #return x + y
# (위와 동일) lambda x, y: x + y



def my_max(lst, cmp = lambda x, y: x if x>y else y):
    max_value = lst[0] #초기 최대값은 리스트의 첫번째 요소 
    for item in lst[1:]: #리스트의 두번째요소부터 순회
        max_value = cmp(max_value, item) # cmp 함수를 이용하여 현재 max 와 순회하며 도는 수 비교
    return max_value #최대값 반환 


def my_min(lst, cmp = lambda x, y: x if x < y else y):
    min_value = lst[0]
    for item in lst[1:]:
        min_value = cmp(min_value, item)
    return min_value


lst = [(1,2), (2,3), (5,3), (19,2), (6,100)]

max_value = my_max(lst, cmp=lambda x,y:x if x[1] > y[1] else y) #두번째요소기준 최대값찾기
print(max_value) 

min_value = my_min(lst, cmp=lambda x,y:x if x[1] < y[1] else y)
print(min_value)



# --------------------------------------------
# 2. sort 구현하기 
# 
# 1) 그냥 순서대로 오름차순으로 정렬하기 
# 2) 오름차순, 내림차순으로 정렬하기 
# 3) 주어진 기준 cmp에 맞춰서 오름차순, 내림차순으로 정렬하기 
# 4) 주어진 기준 cmp가 큰 element를 출력하거나, 같다는 결과를 출력하게 만들기 
# 5) cmp상 같은 경우 tie-breaking하는 함수 넣기 
# --------------------------------------------
number = [1, 3, 5, 9]
list_sm = [(3, 5), (6, 1), (2, 9), 8, 5]
elem = 7


# def sort1(lst):

def get_index(lst, newcard):
    for e in lst:
        if e > newcard:
            return lst.index(e)
    else:
        return len(lst)

print(get_index(number, 7))
    
# def index2(lst, elem):
#     for i, e in enumerate(lst):
#         if e > elem:
#             return i
    
def sort1(lst):
    res = []
    res.append(lst[0])
    for newcard in lst[1:]:
        res.insert(get_index(res, newcard), newcard)
    return res

newlist = [8, 0, -9, -3, 4, 7 , 6]
print(sort1(newlist))
 

# def sort1_insert(lst):
#     res = [lst[0]]

#     for elem in lst[1:]:
#         idx_to_insert = get_insert_index(res, elem)
#         res.insert(idx_to_insert, elem)
    
#     return res 

def get_ASC_index(lst, newcard, upper_to_lower = True, cmp = lambda x, y: x if x > y else y):    #오름차순일 때 index 
    if upper_to_lower == True :
        for i in lst:
            if cmp(i, newcard) == i:
                return lst.index(i)
    else :
        for i in lst :
            if cmp(i, newcard) == newcard:
                return lst.index(newcard)
    
    return len(lst)
        
print(get_ASC_index(number, 11))

def sort2(lst, upper_to_lower = True):
    res = []
    res.append(lst[0])
    for newcard in lst[1:]:
        num = get_ASC_index(res, newcard, upper_to_lower = upper_to_lower)
        res.insert(num, newcard)
        
    return res         

print(sort2(newlist, upper_to_lower=True))


def sort3(lst, upper_to_lower = True, cmp = lambda x, y: x if x > y else y): #오름차순으로 하세요 
    res=[]
    res.append(lst[0])
    for i in lst[1:]:
        
        num = get_ASC_index(res, i, upper_to_lower = upper_to_lower, cmp = cmp)
        res.insert(num, i)

    return res 
    
            
print(sort3(newlist))
 




# def sort4(lst, upper_to_lower = True, cmp = lambda x, y: x):
#     pass 

# def sort5(lst, upper_to_lower = True, cmp = lambda x, y: x, tie_breaker = lambda x, y: random.choice([x,y])):
#     pass 



# --------------------------------------------
# os_file_concept.py 해보고 올 것 
# --------------------------------------------

# --------------------------------------------
# 3. safe pickle load/dump 만들기 
# 
# 일반적으로 pickle.load를 하면 무조건 파일을 읽어와야 하고, dump는 써야하는데 반대로 하면 굉장히 피곤해진다. 
# 이런 부분에서 pickle.load와 pickle.dump를 대체하는 함수 safe_load, safe_dump를 짜 볼 것.  
# hint. 말만 어렵고 문제 자체는 정말 쉬운 함수임.
# --------------------------------------------

def safe_load(pickle_path):
    pass 

def safe_dump(pickle_path):
    pass 


# --------------------------------------------
# 4. 합성함수 (추후 decorator)
# 
# 1) 만약 result.txt 파일이 없다면, 함수의 리턴값을 result.txt 파일에 출력하고, 만약 있다면 파일 내용을 읽어서 
#    '함수를 실행하지 않고' 리턴하게 하는 함수 cache_to_txt를 만들 것. txt 파일은 pickle_cache 폴더 밑에 만들 것.  
# 2) 함수의 실행값을 input에 따라 pickle에 저장하고, 있다면 pickle.load를 통해 읽어오고 없다면 
#    실행 후 pickle.dump를 통해 저장하게 하는 함수 cache_to_pickle을 만들 것. pickle 파일은 pickle_cache 폴더 밑에 만들 것. 
# 3) 함수의 실행값을 함수의 이름과 input에 따라 pickle에 저장하고, 2)와 비슷하게 진행할 것. pickle 파일은 pickle_cache 폴더 밑에, 각 함수의 이름을 따서 만들 것 
# --------------------------------------------

def cache_to_txt(function):
    pass 

def cache_to_pickle(function):
    pass 


