def fib1(n):
    if n < 2: return 1
    else: return fib1(n-1) + fib1(n-2)

def fib2(n):
    
    res = [1, 1]

    if n< 2:
        return 1
    else:
        for i in range(n-2):
            res.apeend(r[-1]) + r[-2]
        return res[-1]
    
if __name__=='__main__':
    from time import time
    n = 30

    begin = time()
    for i in range(n):
        print(fib1(i))
    end = time()

    fib1_time = end - begin

    begin = time()
    for i in range(n):
        pass

