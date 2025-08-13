#처음 내 풀이
"""
def solution(numbers):
    answer=[]
    i=0
    while i <len(numbers):
        answer.append(numbers[i]*2)
        i+=1
    return answer"""

#다른 사람 풀이 참고
def solution(numbers):
    return [num*2 for num in numbers]