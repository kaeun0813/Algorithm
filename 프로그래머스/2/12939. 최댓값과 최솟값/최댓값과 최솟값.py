def solution(s):
    nums=list(map(int, s.split()))  #문자열 -> 정수 변환
    return f"{min(nums)} {max(nums)}"