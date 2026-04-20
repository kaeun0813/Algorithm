from math import sqrt
def solution(brown, yellow):
    total=brown+yellow
    answer = []
    w=h=0
    for h in range(1,int(sqrt(total)+1)):
        if total%h==0: #h가 total의 약수이면
            w=total //h
            if (w-2)*(h-2)==yellow:
                answer.append((w,h))
    return answer[0]