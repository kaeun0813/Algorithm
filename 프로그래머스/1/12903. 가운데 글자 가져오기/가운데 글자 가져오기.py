#처음 코드
"""
def solution(s):
    if len(s)%2==0:
        return s[len(s)//2-1]+s[len(s)//2]
    else:
        return s[len(s)//2]"""
    
#개선 코드
def solution(s):
    return s[(len(s)-1)//2:len(s)//2+1]