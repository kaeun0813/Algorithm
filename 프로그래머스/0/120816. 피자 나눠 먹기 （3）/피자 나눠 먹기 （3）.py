#처음 코드
"""
def solution(slice, n):

    if slice < n:
        if n%slice ==0:
            return n//slice
        else: 
            return n//slice+1
    else: 
        return 1
"""
#개선

def solution(slice, n):
    return ((n - 1) // slice) + 1