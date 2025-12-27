#웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력 ->dfs로 해결

#컴퓨터 수 
com=int(input())
# 간선의 수 
line=int(input())
graph=[[] for _ in range(com+1)]
for i in range(line):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt=0
def dfs(r):
    global cnt
    #현재 노드를 방문 처리
    visited[r]=True
    cnt+=1
    #print("현재 방문",r, "방문 카운트",cnt)
    for i in graph[r]:
        if not visited[i]:
            dfs(i)

visited=[False]*(com+1)

dfs(1)

print(cnt-1) #1 방문 카운트 제외 