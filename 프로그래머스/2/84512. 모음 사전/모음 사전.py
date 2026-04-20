def solution(word):
    count=answer=0

    def dfs(cur):
        nonlocal count,answer
        
        if cur!="":
            count+=1
        if word==cur:
            answer=count
            return
        if len(cur)==5:
            return
        for ch in ['A', 'E', 'I', 'O', 'U']:
            dfs(cur+ch)
    dfs("")
    return answer