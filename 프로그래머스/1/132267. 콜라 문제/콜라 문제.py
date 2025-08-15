def solution(a, b, n):
    total=0
    while n >=a:
        count = n//a  #이번 라운드에서 교환 가능한 횟수
        total+=count*b #count 번 교환으로 받은 콜라 병 수 누적
        n=(n%a)+count*b #남은 병+ 새로받은 병(마신 뒤 빈 병으로 환원)
    return total