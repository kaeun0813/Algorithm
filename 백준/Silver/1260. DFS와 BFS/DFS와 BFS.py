from collections import deque
# n: 정점의 개수, m: 간선의 개수, v: 시작 정점 
n,m,v=map(int,input().split())

graph=[[] for _ in range(n+1)]
for i in range(m):
    u,t=map(int,input().split())
    graph[u].append(t)
    graph[t].append(u)
    
for i in range(1,n+1):
    graph[i].sort()

def dfs(v):
    visited[v]=True
    print(v,end=' ')
    for p in graph[v]:
        if not visited[p]:
            dfs(p)

def bfs(v):
    queue=deque([v])
    visited2[v]=True
    while queue:
        p=queue.popleft()
        print(p, end=' ')
        for i in graph[p]:
            if not visited2[i]:
                queue.append(i)
                visited2[i]=True

               
visited=[False]*(n+1)
visited2=[False]*(n+1)
dfs(v)
print()
bfs(v)