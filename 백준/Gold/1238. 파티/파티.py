import sys, heapq
input=sys.stdin.readline
INF=int(1e9)

n,m,x=map(int,input().split())

graph=[[] for i in range(n+1)]
reverse_graph=[[] for i in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    reverse_graph[b].append((a,c))

def dijkstra(x,graph):
    distance=[INF]*(n+1)
    q=[]
    heapq.heappush(q,(0,x))
    distance[x]=0
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
go=dijkstra(x,graph)
back=dijkstra(x,reverse_graph)
answer=0
for i in range(1,n+1):
    answer=max(answer,go[i]+back[i])
print(answer)