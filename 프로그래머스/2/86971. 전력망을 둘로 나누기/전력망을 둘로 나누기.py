def solution(n, wires):
    answer = int(1e9)
    graph=[[] for _ in range(n+1)]
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    def dfs(node, visited, cut_a,cut_b):
        visited[node]=True #현재 노드 방문 처리
        cnt=1
        for nxt in graph[node]:
            if visited[nxt]:
                continue
            if (node == cut_a and nxt == cut_b) or (node == cut_b and nxt == cut_a):
                continue 
            
            cnt+=dfs(nxt, visited,cut_a,cut_b)
        return cnt
            
    for a,b in wires:
        visited=[False]*(n+1)
        cnt=dfs(a,visited, a,b)
        diff=abs(cnt-(n-cnt))
        answer=min(answer,diff)
        
    return answer