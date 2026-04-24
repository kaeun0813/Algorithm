import heapq
def solution(scoville,K):
    heapq.heapify(scoville)
    count=0
    while scoville[0]<K:
        #음식이 두개 미만이면 불가능
        if len(scoville)<2:
            return -1
        #가장 작은 2개 꺼내기
        new=heapq.heappop(scoville)+heapq.heappop(scoville)*2
        #새 음식 만들기
        heapq.heappush(scoville,new)
        #다시 힙에 넣기
        count+=1
        #count증가
    return count