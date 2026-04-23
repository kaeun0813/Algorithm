from collections import deque
def solution(maps):
    n=len(maps)
    m=len(maps[0])
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    
    def bfs():
        queue=deque([(0,0)])
        while queue:
            x,y=queue.popleft()
            #상하좌우
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if (nx<0 or ny<0 or nx>=n or ny>= m):
                    continue
                if maps[nx][ny]==0:
                    continue
                if maps[nx][ny]==1:#처음 방문하는 길인 경우만
                    maps[nx][ny]=maps[x][y]+1
                    queue.append((nx,ny))
            
    bfs()
    answer=maps[n-1][m-1]
    if answer>1:
        return answer
    else:
        return -1
