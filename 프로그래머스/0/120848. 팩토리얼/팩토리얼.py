def solution(n):
    num=1
    for i in range(1,n+1):
        num*=i
        if num==n:
            return i
        elif num>n:
            return i-1
