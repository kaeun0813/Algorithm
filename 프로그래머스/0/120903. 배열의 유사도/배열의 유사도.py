def solution(s1, s2):
    count = 0
    for x in s1:
        if x in s2:  
            count += 1
    return count
