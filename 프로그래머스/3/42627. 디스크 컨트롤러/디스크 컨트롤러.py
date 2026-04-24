import heapq
def solution(jobs):
    jobs = [(s, l, idx) for idx, (s, l) in enumerate(jobs)]
    jobs.sort()
    wait=[]#대기큐
    i=0
    time=0#현재 시간
    total=0
    n=len(jobs)
    count=0
    
    while count<n:
        #하나씩 꺼낸다.
        while i<n and jobs[i][0]<=time:
            a, b, idx = jobs[i]
            heapq.heappush(wait,(b,a,idx))
            i+=1
        
        if wait:
            b,a,idx=heapq.heappop(wait)
            time+=b
            total+=time-a
            count+=1
        else:
            time=jobs[i][0]
        
        
    return total//n