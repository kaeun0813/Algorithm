"""def solution(lines):
    answer=0
    sorted(lines)
    for i in range(len(lines) - 1):
        if lines[i+1][0] < lines[i][1]:
            answer += min(lines[i][1], lines[i+1][1]) - lines[i+1][0]
    return answer
"""
def solution(lines):
    cover = [0] * 201  # -100..100 → 0..200
    for a, b in lines:
        for x in range(a, b):          # [a, b)
            cover[x + 100] += 1
    return sum(c >= 2 for c in cover)

