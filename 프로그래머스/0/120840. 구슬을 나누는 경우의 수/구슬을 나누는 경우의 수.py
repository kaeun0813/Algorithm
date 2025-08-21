def solution(balls, share):
    num1=num2=1
    for i in range(balls,balls-share,-1):
        num1*=i
    for t in range(1,share+1,1):
        num2*=t
    return num1//num2