from collections import deque

t=int(input()) #테스트 케이스
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(t):
    m,n,k=map(int,input().split())

    graph=[[0]*m for _ in range(n)]

    for _ in range(k):
        x,y=map(int,input().split())
        graph[y][x]=1

    #모든 노드(위치)에 대하여 채우기
    result=0
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                result+=1
                graph[i][j]=0
                queue=deque([(i,j)])
                while queue:
                    x,y=queue.popleft()
                    for d in range(4):
                        nx=x+dx[d]
                        ny=y+dy[d]
                        if nx<=-1 or nx>=n or ny<=-1 or ny>=m or graph[nx][ny]==0:
                            continue
                        if graph[nx][ny]==1:
                            graph[nx][ny]=0
                            queue.append(((nx,ny)))
    print(result)