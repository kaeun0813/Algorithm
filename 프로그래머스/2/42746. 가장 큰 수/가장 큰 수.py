def solution(numbers):    
    #1) 숫자를 문자열로 바꾸기
    nums=list(map(str,numbers))
    #2) 정렬
    nums.sort(key=lambda x: x*3,reverse=True)
    answer=''.join(nums)
    if answer[0]=='0':
        return '0'
    return answer