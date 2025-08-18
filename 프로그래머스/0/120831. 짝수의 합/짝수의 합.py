#처음 코드
"""
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if i%2==0:
            answer+=i
    return answer"""

#개선 코드
def solution(n):
    return sum(range(0, n+1, 2))