# 1은 집이 있는 곳 , 0은 집이 없는 곳
#상하좌우 판단
#출력: 단지수 , 단지 내 속하는 집 수 
n=int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    global cnt
    #주어진 범위를 벗어나면 종료
    if x<=-1 or x>=n or y<=-1 or y>=n:
        return False
    #현재 노드를 방문하지 않았으면, 
    if graph[x][y]==1:
        #해당 노드 방문 처리
        graph[x][y]=0
        cnt+=1
        #상하좌우 재귀적 호출
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

#모든 노드(위치)에 대하여 채우기
result=0
houses=[]
for i in range(n):
    for j in range(n):
        #현재 위치에서 dfs 수행
        cnt=0
        if dfs(i,j)==True:
            result+=1
            houses.append(cnt)
            
print(result)
houses.sort()
for h in houses:
    print(h)