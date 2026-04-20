from itertools import permutations
def solution(k, dungeons):
    def check(order):
        #여기서 한 순서가 몇개 가능한지 계산
        fatigue=k
        count=0
        for dungeon in order:
            #조건 체크
            #가능하면:
            if dungeon[0]<=fatigue:
                fatigue-=dungeon[1]
                count+=1
            else:
                break
        return count
    answer=0
    for order in permutations(dungeons):
        answer=max(answer,check(order))

    return answer