#처음 코드
"""
def solution(n):
    answer = []
    i=1
    while i<=n:
        answer.append(i)
        i+=2
    return answer"""

def solution(n):
    return list(range(1, n+1, 2))