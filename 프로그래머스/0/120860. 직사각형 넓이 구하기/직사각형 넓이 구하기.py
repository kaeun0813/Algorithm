def solution(dots):
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]
    
    width = max(x) - min(x)     # 가로
    height = max(y) - min(y)    # 세로
    
    return width * height
