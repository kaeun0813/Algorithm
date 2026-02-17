import sys
import heapq
input=sys.stdin.readline

n,e=map(int,input().split())
INF=int(1e9)
graph=[[] for _ in range(n+1)]


for _ in range(e):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

u,v=map(int,input().split())

def dijkstar(k):
    distance=[INF]*(n+1)
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
    return distance


dist1=dijkstar(1)
distu=dijkstar(u) #u정점에서 출발 했을때 모든 정점까지의 거리
distv=dijkstar(v) #V정점에서 출발 했을때 모든 정점까지의 거리
path1=dist1[u]+distu[v]+distv[n] # 1->u->v->n
path2=dist1[v]+distv[u]+distu[n] # 1->v->u->n
final=min(path1,path2)


if final>=INF:
    print(-1)
else:
    print(final)