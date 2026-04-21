def solution(array, commands):
    answer = []
    for a,b,c in commands:
        t=array[a-1:b]
        t.sort()
        answer.append(t[c-1])
    return answer