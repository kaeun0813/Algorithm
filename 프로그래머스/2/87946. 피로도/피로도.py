
def solution(k, dungeons):
    #현재 상태에서 아직 안 간 던전 들 중에서 하나 선택
    def dfs(fatigue, count, visited):
        #정답 갱신
        nonlocal answer
        answer=max(answer,count)
        for i in range(len(dungeons)):
            #아직 방문 안했고,
            if not visited[i] and fatigue>=dungeons[i][0]:
                visited[i] = True
                dfs(fatigue-dungeons[i][1], count+1, visited)
                visited[i] = False
    visited=[False]*(len(dungeons))
    answer=0
    dfs(k, 0, visited)
    return answer