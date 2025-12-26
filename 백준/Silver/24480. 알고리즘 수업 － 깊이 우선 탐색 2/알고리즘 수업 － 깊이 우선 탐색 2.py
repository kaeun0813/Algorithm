import sys
input = sys.stdin.readline

#방문 순서 배열을 채워서 1~n 출력
#재귀 말고 스택으로

#n 정점, m 간선, r 시작 정점
n,m,r = map(int,input().split())


graph=[[] for _ in range(n+1)]
for _ in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
#print("그래프 출력",graph)
for i in range(1,n+1):
    graph[i].sort()

#방문 순서 저장 배열
order=[0]*(n+1)
cnt=1

stack=[r] #방문할 후보 쌓아두는 곳
while stack:
    cur=stack.pop()
    if order[cur]!=0: #이미 방문 했으면
        continue #아래 로직을 건너뜀. 
    order[cur]=cnt
    cnt+=1

    #오름차순으로 방문하려면 스택에는 역순으로 넣어야 함
    for nxt in graph[cur]:
        if order[nxt]==0: #아직 방문하지 않은 것만 스택에 추가
            stack.append(nxt)



sys.stdout.write("\n".join(map(str, order[1:])) + "\n")
