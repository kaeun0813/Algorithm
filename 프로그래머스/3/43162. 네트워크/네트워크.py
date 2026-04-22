def solution(n, computers):
    graph=[[] for _ in range(n)]
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if computers[i][j]==1:
                graph[i].append(j)
    def dfs(node,visited):
        cnt=1
        visited[node]=True
        for nxt in graph[node]:
            if visited[nxt]:
                continue
            dfs(nxt,visited)
        return cnt
        
                
    visited=[False]*(n+1)    
    cnt=dfs(0,visited)
    for i in range(n):
        if not visited[i]:
            dfs(i,visited)
            cnt+=1   
    return cnt