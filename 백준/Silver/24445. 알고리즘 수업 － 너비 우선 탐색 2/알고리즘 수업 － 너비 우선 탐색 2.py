
import sys
from collections import deque
input = sys.stdin.readline
# n 정점, m 간선, r 시작 정점
n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    graph[i].sort()

# 방문 순서 저장 배열
order = [0] * (n+1)
cnt = 1


def bfs(r):
    global cnt
    #큐(queue) 구현을 위해 deque 라이브러리 사용
    queue=deque([r])
    order[r]=cnt #시작 정점 방문
    cnt+=1
    #큐가 빌 때까지 반복
    while queue:
        #큐에서 하나의 원소를 뽑아 출력 
        cur =queue.popleft()
        
        #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in reversed(graph[cur]):
            if order[i]==0: #아직 방문 안 했으면
                order[i]=cnt
                cnt+=1
                queue.append(i)


bfs(r)

sys.stdout.write("\n".join(map(str, order[1:])) + "\n")