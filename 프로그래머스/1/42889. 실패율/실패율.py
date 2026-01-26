def solution(N, stages):
    answer = []
    fail=[]
    #전체 플레이어
    total=len(stages)
    for i in range(1,N+1):
        if total>0:
            fail.append((i,stages.count(i)/total))
            total-=stages.count(i)
        else:
            #스테이지에 도달한 사람이 없으면 0으로 고정
            fail.append((i,0))
    fail.sort(key=lambda x: (-x[1],x[0]))
    for i in range(N):
        answer.append(fail[i][0])
    return answer
