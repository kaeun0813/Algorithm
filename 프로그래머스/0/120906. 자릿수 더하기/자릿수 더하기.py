def solution(n):
    answer=[int(num) for num in str(n) if num.isdigit()]
    return sum(answer)