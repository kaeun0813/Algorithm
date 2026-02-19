import sys
input=sys.stdin.readline
INF=int(1e9)
v,e=map(int,input().split())

graph=[[INF]*(v+1) for _ in range(v+1)]

for i in range(1,v+1):
    graph[i][i]=0

for _ in range(e):
    a,b,c=map(int,input().split())
    if c< graph[a][b]: #같은 간선이 여러번 들어올 경위 
        graph[a][b]=c

for k in range(1,v+1):
    for a in range(1,v+1):
        if graph[a][k]==INF:
            continue
        for b in range(1,v+1):
            if graph[k][b]==INF:
                continue
            if graph[a][b]>graph[a][k]+graph[k][b]:
                graph[a][b]=graph[a][k]+graph[k][b]

result=INF
for i in range(1,v+1):
    for j in range(1,v+1):
        if i!=j:
            result=min(result,graph[i][j]+graph[j][i])

if result==INF:
    print(-1)
else:
    print(result)