def solution(order): 
    num='369'
    cnt=0
    for i in str(order):
        if i in num:
            cnt+=1
            print(i)
    return cnt