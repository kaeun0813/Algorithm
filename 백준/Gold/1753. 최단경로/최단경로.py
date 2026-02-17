import sys
import heapq
input=sys.stdin.readline
INF=int(1e9)

n,e=map(int,input().split())
#시작 장점
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

k=int(input())
for _ in range(e):
    u,v,w=map(int,input().split())
    graph[u].append((v,w))
def dijkstra(k):
    q=[]
    heapq.heappush(q,(0,k))
    distance[k]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
                
dijkstra(k)
for i in range(1,n+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])
